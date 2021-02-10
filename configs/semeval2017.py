import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--print_every', type=int, default=20, help='test')
    parser.add_argument('--lr_ratio', type=float, default=0.1, help="subsample threshold")
    parser.add_argument('--lr', type=float, default=0.0003, help="subsample threshold")
    parser.add_argument('--weight_decay', type=float, default=0, help='')
    parser.add_argument('--weight_power', type=float, default=0.75, help='power')
    parser.add_argument('--train_w2v', action='store_true', default=False, help='')
    parser.add_argument('--name', type=str, default='semeval2017', help="model name")
    parser.add_argument('--datapath', type=str, default='data/semeval2017/semeval2017.test.json',
                        help="data directory path")
    parser.add_argument('--dim_embed', type=int, default=200, help="embedding dimension")
    parser.add_argument('--hidden_dim', type=int, default=200, help='hidden dimension')
    parser.add_argument('--bidirectional', action='store_true', default=False)
    parser.add_argument('--neg_ratio', type=float, default=0.5, help="number of negative samples")
    parser.add_argument('--epoch', type=int, default=10, help="number of epochs")
    parser.add_argument('--init_steps', type=int, default=0, help="number of epochs")
    parser.add_argument('--init_stop', type=int, default=10, help="number of epochs")
    parser.add_argument('--update_steps', type=int, default=1000, help="number of epochs")
    parser.add_argument('--mb', type=int, default=32, help="mini-batch size")
    parser.add_argument('--optim', type=str, default='adam', help='optimer')
    parser.add_argument('--do_train', action='store_true', default=False, help='train')
    parser.add_argument('--conti', action='store_true', help="continue learning")
    parser.add_argument('--cuda', action='store_true', default=True, help="use CUDA")
    parser.add_argument('--doc_size', type=int, default=11412, help='testal number of docs')
    parser.add_argument('--avg_dl', type=float, default=26, help="subsample threshold")
    parser.add_argument('--w2vpath', type=str,
                        default='data/All_Words_WSD/Training_Corpora/semcor/labeled_chenvecs.npy',
                        help="path of word embedding")
    parser.add_argument('--data_dir', type=str, default='data/All_Words_WSD/Training_Corpora/semcor/', help='')
    parser.add_argument('--test_path', type=str, default='data/semeval2017/semval2017.test.json', help='')
    parser.add_argument('--train_path', type=str,
                        default='data/semeval2017/semval2017.train.json', help='')
    parser.add_argument('--dev_path', type=str,
                        default='data/semeval2017/semval2017.dev.json' ,help='')
    parser.add_argument('--preds_path', type=str,
                        default='data/semeval2017/use_preds.json')
    parser.add_argument('--negpreds_path', type=str,
                        default='data/All_Words_WSD/Training_Corpora/semcor/labeled_negpreds_emexpand.json')
    parser.add_argument('--attention_k', type=int, default=8)
    parser.add_argument('--model_path', type=str, default=None)
    parser.add_argument('--model_type', type=str, default='wsd3')
    parser.add_argument('--max_len', type=int, default=10000)
    parser.add_argument('--case_study', action='store_true', default=False)
    parser.add_argument('--case_query', type=str, default='')
    parser.add_argument('--case_doc', type=str, default='')
    parser.add_argument('--dropout', type=float, default=0.5)
    parser.add_argument('--min_lr', type=float, default=0.00006)
    parser.add_argument('--lr_decay_rate', type=float, default=0.95)
    parser.add_argument('--lr_warmup_steps', type=float, default=100)
    parser.add_argument('--margin', type=float, default=0.1)
    parser.add_argument('--metric', type=str, default='MAP')
    parser.add_argument('--alpha', type=float, default=1)
    parser.add_argument('--layers', type=int, default=5)
    parser.add_argument('--seed', type=int, default=726)
    parser.add_argument('--weight_k', type=float, default=0.25)
    parser.add_argument('--freeze', type=int, default=90705)
    parser.add_argument('--error_analysis', action='store_true', default=False)
    parser.add_argument('--bert_path', type=str, default='/home/zhangyz/code/pretrained_model/bert_base_uncased')
    parser.add_argument('--max_grad_norm', type=float, default=1.0)
    parser.add_argument('--sample_num', type=int, default=1)
    parser.add_argument('--data_type',type=str,default='only_test')
    parser.add_argument('--eloss_weight', type=float, default=1.0)
    parser.add_argument('--comments', type=str, default='')
    parser.add_argument('--wo_estep', action='store_true', default=False)
    parser.add_argument('--wo_prior', action='store_true', default=False)
    parser.add_argument('--neg_sample', type=str, default='keys')
    parser.add_argument('--local_rank', type=int, default=-1)
    parser.add_argument('--labeled_train_dataloader', type=str,
                        default='data/All_Words_WSD/Training_Corpora/semcor/labeled_train_dataloader.pkl')
    parser.add_argument('--test_train_dataloader', type=str,
                        default='data/All_Words_WSD/Training_Corpora/semcor/test_train_dataloader.pkl')
    parser.add_argument('--test_dataloader', type=str,
                        default='data/All_Words_WSD/Training_Corpora/semcor/test_dataloader.pkl')
    return parser.parse_args(args)
