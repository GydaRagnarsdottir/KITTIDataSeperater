#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:30:04 2019

@author: GydaRagnarsdottir
"""
#import os
import os.path as osp
import shutil

def readSampleNames(sampleNameFile):   
    with open(sampleNameFile,'r') as snf:
        content = snf.readlines()
    sampleNames = [line.strip() for line in content]
    return sampleNames

def getSampleNamePath():
    sampleNamesPath = input('''Please specify the file storing the sample names: ''')
    return sampleNamesPath
 

def getSrcDir():
    srcDirRoot = input('''Please specify the root of your SOURCE root folders: ''')
    assert osp.exists(srcDirRoot),'Path of srcDirRoot does not exit'
    pathImage_2 = srcDirRoot + '/image_2/'
    assert osp.exists(pathImage_2),'Path of source image_2 does not exit'
    pathLabel_2 = srcDirRoot + '/label_2/'
    assert osp.exists(pathLabel_2),'Path of source label_2 does not exit'
    pathVelodyne = srcDirRoot + '/velodyne/'
    assert osp.exists(pathVelodyne),'Path of source Velodyne does not exit'
    return [pathImage_2,pathLabel_2,pathVelodyne]   

def getDesDir():
    desDirRoot = input('''Please specify the root of your DESTINATION root folders: ''')
    assert osp.exists(desDirRoot),'Path of desDirRoot does not exit'
    pathImage_2 = desDirRoot + '/image_2/'
    assert osp.exists(pathImage_2),'Path of destination image_2 does not exit'
    pathLabel_2 = desDirRoot + '/label_2/'
    assert osp.exists(pathLabel_2),'Path of destination label_2 does not exit'
    pathVelodyne = desDirRoot + '/velodyne/'
    assert osp.exists(pathVelodyne),'Path of destination velodyne does not exit'
    return [pathImage_2,pathLabel_2,pathVelodyne]


def getSampleList():
    try:
        sampleNamePath = getSampleNamePath()
        return readSampleNames(sampleNamePath)
    except:FileNotFoundError
    
def copyASample(name,srcDir,desDir):
    imageSrc = srcDir[0] + name + '.png'
    imageDes = desDir[0] + name + '.png'
    labelSrc = srcDir[1] + name + '.txt'
    labelDes = desDir[1] + name + '.txt'
    velodSrc = srcDir[2] + name + '.bin'
    velodDes = desDir[2] + name + '.bin'
    shutil.copyfile(imageSrc,imageDes)
    shutil.copyfile(labelSrc,labelDes)
    shutil.copyfile(velodSrc,velodDes)
    
def copySamples(sampleNames,srcDir,desDir):
    count = 0
    for name in sampleNames:
        copyASample(name,srcDir,desDir)
        count += 1
        if count%20 == 0:
            print('Already copied '+ str(count)+' samples')
            

def main():
    sampleNames = getSampleList()
    srcDir = getSrcDir()
    desDir = getDesDir()
    copySamples(sampleNames,srcDir,desDir)
    print('!!!Finish!!!')
    return 0
if __name__=="__main__":main()