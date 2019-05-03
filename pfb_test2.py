#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pfb Test2
# Generated: Wed May  1 20:00:26 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import osmosdr
import time


class pfb_test2(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Pfb Test2")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 12.8e6

        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0 = firdes.low_pass(1.0, samp_rate, 20000, 5000, firdes.WIN_HAMMING, 6.76)

        self.Noversample = Noversample = 1
        self.M = M = 512

        ##################################################
        # Blocks
        ##################################################
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  M,
        	  (variable_low_pass_filter_taps_0),
        	  Noversample,
        	  100)
        self.pfb_channelizer_ccf_0.set_channel_map(([]))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'soapy=0,driver=remote,remote=tcp://localhost:55132' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(470850000, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, 'localhost', 7355, 1472, True) # Change 'localhost' to IP address of UDP sink
        # self.blocks_rotator_cc_0 = blocks.rotator_cc(-3.14159*0.0375/2.4) # This rotator shifts the center of the band to a 25 kHz boundary so all the pfb channels line up.
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        # self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_channelizer_ccf_0, 0))
        # self.connect((self.osmosdr_source_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.pfb_channelizer_ccf_0, 0))
        for i in range(M-1):
            self.connect((self.pfb_channelizer_ccf_0, i+1), (self.blocks_null_sink_0, i))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.blocks_udp_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_variable_low_pass_filter_taps_0(self):
        return self.variable_low_pass_filter_taps_0

    def set_variable_low_pass_filter_taps_0(self, variable_low_pass_filter_taps_0):
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0
        self.pfb_channelizer_ccf_0.set_taps((self.variable_low_pass_filter_taps_0))

    def get_Noversample(self):
        return self.Noversample

    def set_Noversample(self, Noversample):
        self.Noversample = Noversample

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M


def main(top_block_cls=pfb_test2, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
