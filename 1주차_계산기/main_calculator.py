import modulecal as my

filename=r'./calculator_result.txt'
fp=open(filename,mode='a',encoding="utf-8")

# 클래스명 : Calculator
# 속성 : 제조사,색깔, 모델명, 인스턴스개수
# 기능: printinfo, cal(클래스함수)

class Calculator:
    # 클래스 속성
    MAKER="카시오"
    INSTANCE=0

    # 인스턴스 속성 : 색상, 모델명(비공개)
    def __init__(self,_color,_modelName):
        self.color=_color
        self.__modelName=_modelName
        Calculator.INSTANCE+=1
    
    # getter/setter 메서드
    @property
    def modelName(self):return self.__modelName
    @modelName.setter
    def modelName(self,newName):self.__modelName=newName

    # 인스턴스 메서드
    def printInfo(self):
        print('='*30)
        print(f'제조사 : {Calculator.MAKER}  색상 : {self.color}')
        print('='*30)

        print(f"{'='*30}",file=fp)
        print(f'제조사 : {Calculator.MAKER}  색상 : {self.color}',file=fp)
        print(f"{'='*30}",file=fp)

    # 클래스 메서드
    @classmethod
    def getCalCount(cls):
        print( f'개수 : {Calculator.INSTANCE}' )
        fp.write(f'개수 : {Calculator.INSTANCE}\n')
    
    @classmethod
    def Cal(self):
            
        try:
                
            result=input("숫자 데이터 입력 : ").strip()
            fp.write(result )
            
            if len(result)==0:raise Exception("입력데이터 없음")

            if (not my.neguNumber(result)) and (not result.isdecimal()) and (not my.pointNumber(result)): raise Exception("숫자 데이터가 아님")
            result=float(result)  if my.pointNumber(result) else int(result)
            
            while True:

                operator=input("연산자 입력 : ").strip()   
                fp.write(operator )            
                if len(operator)==0:raise Exception("입력데이터 없음")
                if  operator not in ["+","-","*","/","="] :raise Exception("연산자가 아님")
                elif operator=="=":break


                num=input("숫자 데이터 입력 : ").strip() 
                fp.write(num)

                if len(num)==0:raise Exception("입력데이터 없음")

                if (not my.neguNumber(num)) and (not num.isdecimal()) and (not my.pointNumber(num)): raise Exception("숫자 데이터가 아님")
                num=float(num)  if my.pointNumber(num) else int(num)

                if operator=="+": result=my.plus(result,num)
                elif operator=="-": result=my.minus(result,num)
                elif operator=="*": result=my.multi(result,num)
                elif operator=="/":  result=result/num
              

        except Exception as e:
            print(e)
            print(f'   =>{e}',file=fp)

            return None
         
        return result


 
# 계산기 제조사 : 카시오, 샤프, 유니원, 캐논
mycal=Calculator("검은색",'model-123456')
mycal.printInfo()


youcal=Calculator("빨간색",'model-456789')
youcal.__modelName="model-77777"
print(youcal.__modelName)
print(youcal.__modelName,file=fp)


Calculator.getCalCount()

a=Calculator.Cal()
print(a)
print(a,file=fp)

fp.close()

