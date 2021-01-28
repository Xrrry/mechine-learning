import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf

hw = tf.constant("hello world");

sess = tf.Session()

print (sess.run(hw))

sess.close()