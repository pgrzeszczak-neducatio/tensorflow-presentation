import tensorflow as tf

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)

sess = tf.Session()
print(sess.run([node1, node2]))
