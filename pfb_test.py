#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pfb Test
# Generated: Fri Apr 26 21:02:09 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui
import scipy


class pfb_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pfb Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pfb Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pfb_test")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4.8e6

        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0 = firdes.low_pass(1.0, samp_rate, 20000, 5000, firdes.WIN_HAMMING, 6.76)

        self.Noversample = Noversample = 1
        self.M = M = 192

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/M*Noversample, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  M,
        	  (variable_low_pass_filter_taps_0),
        	  Noversample,
        	  100)
        self.pfb_channelizer_ccf_0.set_channel_map(([1]))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)

        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, 'localhost', 7355, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-3.14159*0.0375/2.4)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 127)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'dump1.cf32', False)
        self.blocks_endian_swap_0 = blocks.endian_swap(2)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-60, 1)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=25000,
        	quad_rate=25000,
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.blocks_endian_swap_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_endian_swap_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.analog_simple_squelch_cc_0, 0))
        for i in range(M-1):
            self.connect((self.pfb_channelizer_ccf_0, i+1), (self.blocks_null_sink_0, i))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pfb_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.M*self.Noversample)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_variable_low_pass_filter_taps_0(self):
        return self.variable_low_pass_filter_taps_0

    def set_variable_low_pass_filter_taps_0(self, variable_low_pass_filter_taps_0):
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0
        self.pfb_channelizer_ccf_0.set_taps((self.variable_low_pass_filter_taps_0))

    def get_Noversample(self):
        return self.Noversample

    def set_Noversample(self, Noversample):
        self.Noversample = Noversample
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.M*self.Noversample)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.M*self.Noversample)


def main(top_block_cls=pfb_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    tps = scipy.float64(gr.high_res_timer_tps())

    print(tb.pfb_channelizer_ccf_0.pfb.pc_work_time_total()/tps)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
