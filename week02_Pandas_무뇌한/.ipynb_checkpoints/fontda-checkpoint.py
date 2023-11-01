{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1c6ed7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import font_manager, rc\n",
    "\n",
    "font_path=\"무뇌한\\\\NanumGothic.ttf\" #한글 폰트 인스턴스 생성 C:\\Users\\Administrator\\Desktop\\ex_pandas\\무뇌한\\NanumGothic.ttf\n",
    "#font_name=font_manager.FontProperties(fname=font_path).get_name() #요거는 객체\n",
    "#print(font_name)\n",
    "\n",
    "rc('font',family=\"NanumGothics2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c0b92b6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pisa():\n",
    "    import pandas as pd\n",
    "    pisa = pd.DataFrame([[536.5, 518.5, 514.5]], index=['대한민국'], columns=[2012, 2015, 2018])\n",
    "    return pisa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "142d1cc4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
