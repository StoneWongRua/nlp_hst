import  tensorflow as tf

class TextConfig():

    embedding_size=100     # 词向量维度
    vocab_size=8000        # 词汇大小
    pre_trianing = None   # 使用由word2vec训练的字符向量

    seq_length=600         # 序列长度
    num_classes=10         # 类别数

    num_filters=128        # 卷积核数目
    filter_sizes=[2,3,4]   # 卷积核的大小


    keep_prob=0.5          # droppout保留比例
    lr= 1e-3               # 学习率
    lr_decay= 0.9          # 学习率衰减
    clip= 6.0              # 梯度限幅阈值
    l2_reg_lambda=0.01     # l2正则化lambda

    num_epochs=10          # 总迭代轮次
    batch_size=64         # 每批训练大小
    print_per_batch =100   # 输出结果

    train_filename=r'C:\Users\15845\cnews.train.txt'  #train data
    test_filename=r'C:\Users\15845\cnews.test.txt'    #test data
    val_filename=r'C:\Users\15845\cnews.val.txt'      #validation data
    vocab_filename=r'C:\Users\15845\vocab.txt'        #vocabulary
    vector_word_filename=r'C:\Users\15845\vector_word.txt'  #vector_word trained by word2vec
    vector_word_npz=r'C:\Users\15845\vector_word.npz'   # save vector_word to numpy file

class TextCNN(object):

    def __init__(self,config):

        self.config=config

        # 五个待输入的数据
        self.input_x=tf.placeholder(tf.int32,shape=[None,self.config.seq_length],name='input_x')
        self.input_y=tf.placeholder(tf.float32,shape=[None,self.config.num_classes],name='input_y')
        self.keep_prob=tf.placeholder(tf.float32,name='dropout')
        self.global_step = tf.Variable(0, trainable=False, name='global_step')
        self.l2_loss = tf.constant(0.0)

        self.cnn()

    def cnn(self):
        '''CNN模型'''
        # 词向量映射
        with tf.device('/cpu:0'):
            self.embedding = tf.get_variable("embeddings", shape=[self.config.vocab_size, self.config.embedding_size],
                                             initializer=tf.constant_initializer(self.config.pre_trianing))
            self.embedding_inputs= tf.nn.embedding_lookup(self.embedding, self.input_x)
            self.embedding_inputs_expanded = tf.expand_dims(self.embedding_inputs, -1)

        with tf.name_scope('cnn'):
            # CNN layer
            pooled_outputs = []
            for i, filter_size in enumerate(self.config.filter_sizes):
                with tf.name_scope("conv-maxpool-%s" % filter_size):

                    filter_shape = [filter_size, self.config.embedding_size, 1, self.config.num_filters]
                    W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
                    b = tf.Variable(tf.constant(0.1, shape=[self.config.num_filters]), name="b")
                    conv = tf.nn.conv2d(
                        self.embedding_inputs_expanded,
                        W,
                        strides=[1, 1, 1, 1],
                        padding="VALID",
                        name="conv")
                    h = tf.nn.relu(tf.nn.bias_add(conv, b), name="relu")
                    pooled = tf.nn.max_pool(
                        h,
                        ksize=[1, self.config.seq_length - filter_size + 1, 1, 1],
                        strides=[1, 1, 1, 1],
                        padding='VALID',
                        name="pool")
                    pooled_outputs.append(pooled)

            num_filters_total = self.config.num_filters * len(self.config.filter_sizes)
            self.h_pool = tf.concat(pooled_outputs, 3)
            self.outputs= tf.reshape(self.h_pool, [-1, num_filters_total])


        with tf.name_scope("dropout"):
            self.final_output = tf.nn.dropout(self.outputs, self.keep_prob)

        with tf.name_scope('output'):
            fc_w = tf.get_variable('fc_w', shape=[self.final_output.shape[1].value, self.config.num_classes],
                                   initializer=tf.contrib.layers.xavier_initializer())
            fc_b = tf.Variable(tf.constant(0.1, shape=[self.config.num_classes]), name='fc_b')
            self.logits = tf.matmul(self.final_output, fc_w) + fc_b

            # 分类器
            self.prob=tf.nn.softmax(self.logits)
            self.y_pred_cls = tf.argmax(self.logits, 1, name='predictions')

        with tf.name_scope('loss'):
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits, labels=self.input_y)
            self.l2_loss += tf.nn.l2_loss(fc_w)
            self.l2_loss += tf.nn.l2_loss(fc_b)
            self.loss = tf.reduce_mean(cross_entropy) + self.config.l2_reg_lambda * self.l2_loss
            self.loss = tf.reduce_mean(cross_entropy)

        with tf.name_scope('optimizer'):
            # 损失函数，交叉熵
            optimizer = tf.train.AdamOptimizer(self.config.lr)
            gradients, variables = zip(*optimizer.compute_gradients(self.loss))
            gradients, _ = tf.clip_by_global_norm(gradients, self.config.clip)
            # 优化器
            self.optim = optimizer.apply_gradients(zip(gradients, variables), global_step=self.global_step)

        with tf.name_scope('accuracy'):
            # 准确率
            correct_pred=tf.equal(tf.argmax(self.input_y,1),self.y_pred_cls)
            self.acc=tf.reduce_mean(tf.cast(correct_pred,tf.float32))