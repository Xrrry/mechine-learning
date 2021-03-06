import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf

w = tf.Variable(2.0, dtype=tf.float32, name="weight")
b = tf.Variable(1.0, dtype=tf.float32, name="bias")
x = tf.placeholder(dtype=tf.float32, name="input")

with tf.name_scope("output"):
    y = w * x + b

path = "./log"

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(path, sess.graph)
    result = sess.run(y, {x: 3.0})
    print("y = %s" % result)