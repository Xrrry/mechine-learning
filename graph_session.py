import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf

const1 = tf.constant([[2, 2]])
const2 = tf.constant([[4], [4]])

multiple = tf.matmul(const1, const2)

print(multiple)

sess = tf.Session()
result = sess.run(multiple)
print(result)
if const1.graph is tf.get_default_graph():
    print("1是默认")
sess.close()

# 第二种方法
with tf.Session() as sess:
    result2 = sess.run(multiple)
    print(result2)

