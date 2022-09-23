import os

print(os.name) #파이썬이 실행되는 운영체제의 이름
print(os.getcwd()) #현재 작업 디렉토리
print(os.path.join(os.getcwd(), 'test')) #os.path.join(경로1, 경로2)
# print(os.mkdir(os.path.join(os.getcwd(), 'test'))) # 디렉토리를 만듬
# print(os.remove(os.path.join(os.getcwd(), 'text.txt'))) #파일경로의 파일 삭제
# print(os.rmdir(os.path.join(os.getcwd(), 'test'))) #디렉토리 삭제
print(os.listdir(os.getcwd())) #경로 내에 포함된 파일과 디렉토리를 리스트 형태로 반환

