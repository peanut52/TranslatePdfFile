import pathlib
import pdfplumber
import time
import os
import sys
import logging
from configparser import ConfigParser
from concurrent.futures import ProcessPoolExecutor

from pdf2docx import Converter

# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice
# from pdfminer.layout import LAParams, LTTextBox, LTFigure, LTImage
# from pdfminer.converter import PDFPageAggregator
#
f_path = 'PredictingVolatility_LazardResearch_en.pdf'


# with open(f_path, 'rb') as f:
#     parser = PDFParser(f)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     laparams = LAParams()
#     device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     for page in PDFPage.create_pages(doc):
#         interpreter.process_page(page)
#         layout = device.get_result()
#         for x in layout:
#             # 获取文本对象
#             if isinstance(x, LTTextBox):
#                 print(x.get_text().strip())
#             # 获取图片对象
#             if isinstance(x, LTImage):
#                 print('这里获取到一张图片')
#             # 获取 figure 对象
#             if isinstance(x, LTFigure):
#                 print('这里获取到一个 figure 对象')


def keep_time(func):
    def wrapped(*args, **kwargs):
        # mysql_logger.debug('MySQL加锁...')
        ts1 = time.time()
        # mysql_logger.debug('MySQL加锁成功')
        res = func(*args, **kwargs)
        print('->', time.time() - ts1)
        return res

    return wrapped

def check_paragraph(last_sentence, end_sentence):
    if last_sentence.endwith('.'):
        return True
    elif end_sentence.startwith('  '):
        return False
    else:
        return False


@keep_time
def pdf_to_docx(file_path, output_file):
    with pdfplumber.open(file_path) as pdf, open(output_file, 'a', encoding='utf-8') as txt:
        for page in pdf.pages:
            text_data = page.extract_text()
            print(text_data)
            txt.write(text_data)

#encoding : utf-8

import PyPDF4
# import optparse
# from PyPDF4 import PdfFileReader
#
# def printMeta(filename):
#    pdfFile = PdfFileReader(open(filename, 'rb'))
#    docInfo = pdfFile.getDocumentInfo()
#    print('[*] PDF MetaData For: {}'.format(filename))
#    for metaItem in docInfo:
#       print('[+] {0} : {1}'.format(metaItem, docInfo[metaItem]))
#
#
# def main(file_name):
#    parser = optparse.OptionParser('usage %prog + -F CMU-CS-95-113.pdf')
#    parser.add_option('-F' , dest='filename' , type='string' , help='specify PDF file name')
#    (options, args) = parser.parse_args()
#    fileName = options.filename
#    if fileName == None:
#       print(parser.usage)
#       exit(0)
#    else:
#       printMeta(fileName)
#
# if __name__ == '__main__':
#     main(f_path)
# def pdf_to_word(pdf_file_path, word_file_path):
#     cv = Converter(pdf_file_path)
#     cv.convert(word_file_path)
#     cv.close()


# def main():
#     logging.getLogger().setLevel(logging.ERROR)
#
#     config_parser = ConfigParser()
#     # config_parser.read("config.cfg")
#     # config = config_parser["default"]
#
#     tasks = []
#     with ProcessPoolExecutor(max_workers=int(10)) as executor:
#         for file in os.listdir():
#             extension_name = os.path.splitext(file)[1]
#             if extension_name != ".pdf":
#                 continue
#             file_name = os.path.splitext(file)[0]
#             pdf_file = f_path
#             word_file = 'pdf_file.docx'
#             print("正在处理: ", file)
#             result = executor.submit(pdf_to_word, pdf_file, word_file)
#             print(result)
#             tasks.append(result)
#     while True:
#         exit_flag = True
#         for task in tasks:
#             if not task.done():
#                 exit_flag = False
#         if exit_flag:
#             print("完成")
#             exit(0)


# if __name__ == "__main__":
#     main()
# TODO:缺少处理判断行是否结束，并连接多行的部分
if __name__ == '__main__':
    pdf_to_docx(f_path, 'pdf_file.docx')
