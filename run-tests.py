import os
from os import listdir
from os.path import isfile, join


# run the build with maven
def run_build_script( fileIndex, testFilePath ):

    print 'Clean test files at ' + projectTestSrcFolderPath
    projectTestSrcFolderPathForRm = projectTestSrcFolderPath + "*"
    print projectTestSrcFolderPathForRm
    cmd = 'rm -rf ' + projectTestSrcFolderPathForRm
    os.system(cmd)

    print 'Copy the file ' + testFilePath + ' to '
    cmd = 'cp ' + testFilePath + ' ' + projectTestSrcFolderPath
    os.system(cmd)    

    print 'Run mvn clean ...'
    cmd = 'mvn -f ' + projectFolderPath + 'pom.xml clean'
    os.system(cmd)

    print 'Run mvn cobertura:cobertura'
    cmd = 'mvn -f ' + projectFolderPath + 'pom.xml cobertura:cobertura'
    os.system(cmd)

    print 'Create folder '
    cmd = 'mkdir -p ' + outputReportFolderPath + '/' + str(index)
    os.system(cmd)

    print 'Copy the result to directory'
    cmd = 'cp -r ' + projectFolderPath + 'target/site/* ' + outputReportFolderPath + '/' + str(index) + '/'
    os.system(cmd)

    return


# main program entrance
inputTestFolderPath = './inputs/'
outputReportFolderPath = './outputs/'
projectFolderPath = '/Users/yusun/workspace/junitbook2/code-coverage/'
projectTestSrcFolderPath = '/Users/yusun/workspace/junitbook2/code-coverage/src/test/java/edu/csupomona/cs585/'

index = 0;
for f in listdir(inputTestFolderPath):    
    fileFullPath = join(inputTestFolderPath,f)
    if (isfile(fileFullPath) and fileFullPath.endswith('.java')):        
        index = index + 1
        run_build_script(index, fileFullPath)
