import sys, os
from gensim.models import Word2Vec
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
import numpy as np
from odps.df import DataFrame
import pandas as pd
from pypai.io import TableReader

# # sentence = [['我们', '阿在', 'tt'],['黄河', '之水', '天上来', '</s>']]
# # dimention = 100 # 词向量维数
# # model100 = gensim.models.Word2Vec(sentence, sg=0,size=dimention, min_count=0, window=5)#训练词向量
# # model100.save(r'C:\Users\koma.lwz\Desktop\test/word2vec_model_100')
#
# def visualize(model, output_path):
#     meta_file = "w2x_metadata.tsv"
#     placeholder = np.zeros((len(model.wv.index2word), 100))
#
#     with open(os.path.join(output_path,meta_file), 'wb') as file_metadata:
#         for i, word in enumerate(model.wv.index2word):
#             placeholder[i] = model[word]
#             # temporary solution for https://github.com/tensorflow/tensorflow/issues/9094
#             if word == '':
#                 print("Emply Line, should replecaed by any thing else, or will cause a bug of tensorboard")
#                 file_metadata.write("{0}".format('<Empty Line>').encode('utf-8') + b'\n')
#             else:
#                 file_metadata.write("{0}".format(word).encode('utf-8') + b'\n')
#
#     # define the model without training
#     sess = tf.InteractiveSession()
#
#     embedding = tf.Variable(placeholder, trainable = False, name = 'w2x_metadata')
#     tf.global_variables_initializer().run()
#
#     saver = tf.train.Saver()
#     writer = tf.summary.FileWriter(output_path, sess.graph)
#
#     # adding into projector
#     config = projector.ProjectorConfig()
#     embed = config.embeddings.add()
#     embed.tensor_name = 'w2x_metadata'
#     embed.metadata_path = meta_file
#
#     # Specify the width and height of a single thumbnail.
#     projector.visualize_embeddings(writer, config)
#     saver.save(sess, os.path.join(output_path,'w2x_metadata.ckpt'))
#     # print('Run `tensorboard --logdir={0}` to run visualize result on tensorboard'.format(output_path))

def my_visualize(tokens, embs, output_path):
    meta_file = "w2v_metadata.tsv"
    placeholder = np.zeros((len(tokens), len(embs[0])))

    with open(os.path.join(output_path,meta_file), 'wb') as file_metadata:
        for i, emb in enumerate(embs):
            placeholder[i] = emb
            # temporary solution for https://github.com/tensorflow/tensorflow/issues/9094
            if tokens[i] == '':
                print("Emply Line, should replecaed by any thing else, or will cause a bug of tensorboard")
                file_metadata.write("{0}".format('<Empty Line>').encode('utf-8') + b'\n')
            else:
                file_metadata.write("{0}".format(tokens[i]).encode('utf-8') + b'\n')

    # define the model without training
    sess = tf.InteractiveSession()

    embedding = tf.Variable(placeholder, trainable = False, name = 'w2v_metadata')
    tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(output_path + 'w2v', sess.graph)

    # adding into projector
    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = 'w2v_metadata'
    embed.metadata_path = meta_file
    print('will write...')
    # Specify the width and height of a single thumbnail.
    projector.visualize_embeddings(writer, config)
    saver.save(sess, os.path.join(output_path + 'w2v','w2v_metadata.ckpt'))
    # print('Run `tensorboard --logdir={0}` to run visualize result on tensorboard'.format(output_path))

def get_w2v(odps_path):
    # 'hm_tech_dev.hm_emb_fliter_emoji'
    reader = tf.python_io.TableReader(odps_path)
    total_records_num = reader.get_row_count() # return 3
    batch_size = 500
    iter_nums = total_records_num//batch_size + 1
    tokens = []
    embs = []

    for i in range(iter_nums):
        records = reader.read(batch_size)
        for record in records:
            tokens.append(record[0])
            embs.append(record[1])
    reader.close()

    return tokens, embs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PAI tensorboard')

    parser.add_argument('--odps_path', default='odps://hm_tech_dev/tables/hm_emb_fliter_emoji',
                        required=True,
                        help='odps path')
    parser.add_argument('--checkpointDir', default='oss://muxing-tf-proj/?host=oss-cn-zhangjiakou&role_arn=acs:ram::1884461636387355:role/tensorboard',
                        required=False,
                        help='odps access_id')
    args, ukown = parser.parse_known_args()

    tokens, embs = get_w2v(args.odps_path)
    print('get token&emb done!')
    my_visualize(tokens, embs, args.checkpointDir)

