# File: cache.py
# Author(s): Alex Burdick, Dean Orenstein
# Date: 04/30/2020
# Section: 511
# E-mail: burdick.alex@tamu.edu, dean27@tamu.edu
# Description:
# e.g. The content of this file implements ...

class Cache:
    def __init__(self, ram, blockSize, associativity, replacementPolicy, writeHitPolicy, writeMissPolicy):
        this.ram = ram
        this.blockSize = blockSize
        this.associativity = associativity
        this.replacementPolicy = replacementPolicy
        this.writeHitPolicy = writeHitPolicy
        this.writeMissPolicy = writeMissPolicy

    def cacheRead(self):
        pass

    def cacheWrite(self):
        pass

    def cacheView(self):
        pass

    def memoryView(self):
        pass

    def cacheDump(self):
        pass

    def memoryDump(self):
        pass

