from src import util
import Configurations as conf
import subprocess
import os


def filterInput():
    util.generateDirectories(conf.filteredDir)
    filenames = os.listdir(conf.inputFolder)
    for filename in filenames:
        with open(os.path.join(conf.filteredDir, filename), "w") as wf, \
                open(os.path.join(conf.inputFolder, filename), "r") as rf:
            for line in rf:
                arr = line.split("\t")
                if arr[0] != arr[1]:
                    wf.write(line)


def convertResultToCPickleDict():
    util.generateDirectories(conf.cPickleDir)
    filenames = os.listdir(conf.resultFolder)
    for filename in filenames:
        with open(os.path.join(conf.resultFolder, filename), "r") as f:
            for line in f:



def main():
    filterInput()

    filenames = os.listdir(conf.filteredDir)

    util.generateDirectories(conf.resultFolder)

    for filename in filenames:
        fileDir = os.path.join(conf.filteredDir, filename)

        cmd = [conf.mosaicFinderDir, "-e", "1e-05", "-p", "30", "-i", fileDir, "-o", os.path.join(conf.resultFolder, filename)]

        proc = subprocess.Popen(cmd)

    return 0


if __name__ == '__main__':
    main()
