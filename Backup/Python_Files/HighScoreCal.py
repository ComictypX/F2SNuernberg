{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/home/kraken/Pictures'"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import os\n",
    "#cmd = 'curl -X GET -s -k -H \"Content-Type: application/json\" --key ../client_certs/RESTTEST_key.pem --cert ../client_certs/RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat query.json | base64 -w 0)'\n",
    "#os.system(cmd)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### GPS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"gpsData.json\", \"r+\") as jsonFile:\n",
    "    dataDict = json.load(jsonFile)\n",
    "    data = dataDict['result']['data']\n",
    "#nextItem=dataDict['result']['next-item']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "# get zeros\n",
    "ze=[]\n",
    "for index, row in enumerate(data):\n",
    "    if row[5]==0:\n",
    "        ze.append(index)\n",
    "# check consecutive zeros        \n",
    "element=[]\n",
    "for index, value in enumerate(ze):\n",
    "    if ze[index]-ze[index-1]==1:\n",
    "        element.append(value-1) \n",
    "        # here value is index of elements with zero velocity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [],
   "source": [
    "impData=[]\n",
    "for index, value in enumerate(data):\n",
    "    if index not in ze:\n",
    "        impData.append((int(data[index][1]),data[index][5]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(815, 2)"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.shape(impData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(641438873, 0.1241165791411044, 79.61319864488532)"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avgVel=np.mean(impData,axis=0)[1]\n",
    "timeDiff = abs(impData[0][0]-impData[-1][0])\n",
    "dist = avgVel*timeDiff/1e6\n",
    "timeDiff, avgVel, dist"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Battery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"batteryData.json\", \"r+\") as jsonFile:\n",
    "    batDict = json.load(jsonFile)\n",
    "    batData = batDict['result']['data']\n",
    "#nextItem=dataDict['result']['next-item']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [],
   "source": [
    "impBatData=[]\n",
    "for index, value in enumerate(batData):\n",
    "    if index not in ze:\n",
    "        impBatData.append(batData[index][5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(impBatData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "cmd = 'curl -X GET -s -k -H \"Content-Type: application/json\" --key ../client_certs/RESTTEST_key.pem --cert ../client_certs/RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat query.json | base64 -w 0)'\n",
    "a=os.system(cmd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14848"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hsData={'dist':dist, 'bat_charge':10}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('highscore.txt', 'w') as hs:\n",
    "    hs.write(str(np.around(dist, decimals=3)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
