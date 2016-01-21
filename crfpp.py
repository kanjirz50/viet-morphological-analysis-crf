#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

class CRF_PP:
    def __init__(self, model_file_path):
        """Initialize CRF"""
        self.crf_model_path = model_file_path
        self.cmd = ('crf_test', '-m', self.crf_model_path)

    def analyze(self, sentence):
        """analyze sentence"""
        p = subprocess.Popen(self.cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # End of 2 elements are empty. They are deleted
        yamcha_result = p.communicate(self.sentence2iob_format(sentence))[0].split('\n')[:-2]
        return self.crf_result2iob_format(yamcha_result)

    def sentence2iob_format(self, sentence):
        """convert format from sentence to IOB2 format"""
        syllables = sentence.split(' ')
        # crf++ needs the symbol of end of sentence.
        syllables.append('')
        return '\n'.join(syllables)

    def crf_result2iob_format(self, yamcha_result):
        """Conver crf++ result into IOB2tag tuples."""
        return [(line.rstrip().split('\t')) for line in yamcha_result]


def main():
    """Usage"""
    crf_p = CRF_PP("./test_crfmodel.model")

    sentences = (
        "Cách đây dúng 1 tháng , Liverpool ngậm ngùi nhìn M.U lấy 3 điểm ở PL sau khi dể lọt lưới ở phút bù giờ sau pha đánh đầu của trung vệ Rio Ferdinand , thất bại khiến .",
    )

    for sentence in sentences:
        for lemma, iobtag in crf_p.analyze(sentence):
            print lemma, iobtag

if __name__ == "__main__":
    main()
