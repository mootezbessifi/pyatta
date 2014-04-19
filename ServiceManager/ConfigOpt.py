#!/usr/bin/env python
    
import sys
import os
topdir = os.path.dirname(os.path.realpath(__file__)) + "../.."
topdir = os.path.realpath(topdir)
sys.path.insert(0, topdir)
from ExecFormat.execformat import execUtils
class config_opt():
    exe=execUtils()

    def set(self, args):
        args.insert(0,'set')
        try:
            self.exe.execmd(args)
            return True
        except OperationFailed,e:
            return e.message 

    def delete(self, args):
        args.insert(0,'delete')
        try:
            self.exe.execmd(args)
            return True
        except OperationFailed,e:
            return e.message
