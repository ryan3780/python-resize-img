import os
import glob
from PIL import Image
import zipfile
import shutil

#  현재 디렉토리에 있는 zip파일만 리스트로 만들기
zips = glob.glob('*.zip')

# 모든 zip파일을 원하는 경로에 압축 풀기
def unziped(zipFile, path):
    with zipfile.ZipFile(zipFile, 'r') as existing_zip:
            existing_zip.extractall(path)

# 압축 파일 중 구조가 다른 압축 파일은 새로운 디렉토리를 만들어서 같은 구조로 압축 풀기
def createDir(zip):
    os.makedirs('unzip_dir/' + zip.replace(".zip", "") + '_jpg')
    zipPath = 'unzip_dir/' + zip.replace(".zip", "") + '_jpg'
    if os.path.exists(zipPath):
        unziped(zip, zipPath)

# zip파일 리스트의 길이 만큼 조건에 맞춰서 압축 해제하기
for i in range(len(zips)):

    if '_1' in zips[i]:
        createDir(zips[i])
    elif '_2' in zips[i]:
        createDir(zips[i])
    elif '_3' in zips[i]:
        createDir(zips[i])
    else:
        unziped(zips[i], 'unzip_dir')
        
# 각각의 폴더 안에 특정 경로에 있는 jpg 파일들의 사이즈를 80 x 100 으로 변경하기
def resizeJpg(jpgPath):
    for f in jpgPath:
        img = Image.open(f)
        img_resize = img.resize((int(80), int(100)))
        title, ext = os.path.splitext(f)
        img_resize.save(title + ext)

# 압축이 해제된 폴더들이 있는 경로에서 한번 더 들어가기
files = glob.glob('unzip_dir/*', recursive=True)

# 폴더 안에 특정 경로를 조건에 맞춰서 들어가서 원하는 jpg파일들의 사이즈 변경
for dir in files:

    if '_1' in dir:
        jpgPath = glob.glob(dir + '/ops/page_thumbnails/*.jpg')
        resizeJpg(jpgPath)
    elif '_2' in dir:
        jpgPath = glob.glob(dir + '/ops/page_thumbnails/*.jpg')
        resizeJpg(jpgPath)
    elif '_3' in dir:
        jpgPath = glob.glob(dir + '/ops/page_thumbnails/*.jpg')
        resizeJpg(jpgPath)
    else: 
          subDir = glob.glob(dir + '/*', recursive=True)

          if len(subDir) == 1:
              jpgPath = glob.glob(subDir[0] + '/ops/page_thumbnails/*.jpg')
              resizeJpg(jpgPath)
          elif len(subDir) == 2:
              first_jpgPath = glob.glob(subDir[0] + '/ops/page_thumbnails/*.jpg')
              second_jpgPath = glob.glob(subDir[1] + '/ops/page_thumbnails/*.jpg')
              resizeJpg(first_jpgPath)
              resizeJpg(second_jpgPath)
          else:
              first_jpgPath = glob.glob(subDir[0] + '/ops/page_thumbnails/*.jpg')
              second_jpgPath = glob.glob(subDir[1] + '/ops/page_thumbnails/*.jpg')
              third_jpgPath = glob.glob(subDir[2] + '/ops/page_thumbnails/*.jpg')

# 위에 있는 코드들이 다 실행 되고 나서, 모든 폴더들의 이름을 변경하기
for f in files:
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + '(썸네일 변경 완료)' + fext)