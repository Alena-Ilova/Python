{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ecd7f678-0407-46f6-b994-ba7a83153284",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "greeting=\"Hello\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e5319f8-7bf3-4be8-831f-7d612f924ef4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print(greeting)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "477fb599-4125-4279-b618-8fa4e563f852",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "register = 50        # An integer assignment\n",
    "miles   = 100       # A floating point\n",
    "name    = \"Mike\"    # A string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3129d6f5-8e8d-4287-bd55-b2b05247e604",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "100\n",
      "Mike\n"
     ]
    }
   ],
   "source": [
    "print(register)\n",
    "print(miles)\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "346c471a-e88c-4826-a3e3-67cb044006b7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 7\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "b=2\n",
    "c=7\n",
    "print (a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0b311024-ac31-4a57-b7ee-2c32e4e12328",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1 1\n"
     ]
    }
   ],
   "source": [
    "a=b=c=1\n",
    "print (a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1cbca9a2-5c8b-4141-bcd0-1aa7ca1afa2d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 6 john\n"
     ]
    }
   ],
   "source": [
    "a,b,c=1,6,\"john\"\n",
    "print (a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2516322f-42b0-42e4-8de8-b568886814d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "PI=3.1415\n",
    "GRAVITY=9.8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e9201aad-9b8a-447b-a5e1-95027cd7ef70",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x= 6  t= 301.8333333333333\n"
     ]
    }
   ],
   "source": [
    "x=6\n",
    "y=9\n",
    "z=2\n",
    "t=(x+y)*20+(y+z)/x\n",
    "print ('x=',x,' t=',t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b503cecc-b5a3-4892-98f7-aabd6512b7d1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "strings = 'This is Python'\n",
    "char = \"A\"\n",
    "multiline_str = '''This is a string with some code.'''\n",
    "my_string='multiline \\n string'\n",
    "raw_str = r'raw \\n string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "581c6e6f-f05d-4538-82e4-37aa9931a526",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is Python\n",
      "A\n",
      "This is a string with some code.\n"
     ]
    }
   ],
   "source": [
    "print(strings)\n",
    "print(char)\n",
    "print(multiline_str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "dbfcf7eb-9a99-45b6-8626-156044444f97",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "strings = 'This is Python'\n",
    "char = \"A\"\n",
    "multiline_str = '''This is \n",
    "a string\n",
    "with \n",
    "some code.'''\n",
    "my_string='multiline \\n string'\n",
    "raw_str = r'raw \\n string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4bb5f1f4-814d-4245-b069-6183740ce852",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is Python\n",
      "A\n",
      "This is \n",
      "a string\n",
      "with \n",
      "some code.\n"
     ]
    }
   ],
   "source": [
    "print(strings)\n",
    "print(char)\n",
    "print(multiline_str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9be4f107-d711-41ae-aee2-39d658e73eff",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "unicode = u'\\u00dcnic\\u00f6de'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "528aff18-1134-4f73-8117-49360eb20d98",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ünicöde\n"
     ]
    }
   ],
   "source": [
    "print(unicode)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ba3d384a-6606-418c-b569-86f5929d5a89",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_string='multiline \\\\n string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "8923a667-8e5c-481e-a99e-45866b2a817a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "multiline \\n string\n"
     ]
    }
   ],
   "source": [
    "print(my_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "068502b2-60e9-43c8-8913-ddb428d10650",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "raw_astr = r'raw \\n string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "73f3a880-3ca3-49ee-9bb6-41db6c1f3b21",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "raw \\n string\n"
     ]
    }
   ],
   "source": [
    "print(raw_astr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "9dc45fd2-7005-41e5-817b-04760c7faf7b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "x=(5>8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ba168717-83fa-4b9c-841a-a27cd2ef326d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "54f13538-5381-4282-89a4-0b311a0fe00d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "y=(5748<39840)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c5792433-7c7e-4ca0-bce8-a05e10f2e842",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "p=(9==2+7)\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "8f0a8420-8a1c-417f-953b-a1465f0ffa14",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "a=False+8\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "ab8d69eb-0312-4f25-82e9-698b1a337c18",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "fruits = ['pineapple', 'coco', 'mango'] #list\n",
    "numbers = (1 , 2, 3) #tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "392fa60e-94d9-4ad5-9e07-cc8497c6a2a9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pineapple', 'coco', 'mango']\n",
      "(1, 2, 3)\n"
     ]
    }
   ],
   "source": [
    "print(fruits)\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "bad0beac-b68c-4c56-82e3-491d35940355",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "family = ['mother', 'brother', 'father', 'sister'] #list\n",
    "numbers = (8, 11, 14, 17) #tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "c552c64c-57bf-45dd-b8a1-56c1e7e65978",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mother', 'brother', 'father', 'sister']\n",
      "(8, 11, 14, 17)\n"
     ]
    }
   ],
   "source": [
    "print(family)\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "dc007156-2d7d-4fe3-a66e-2394324ea9eb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_list=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "49e10396-deb3-4598-b984-d0d577f906fc",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[14, 14, 14, 'This is a wonderful day']\n"
     ]
    }
   ],
   "source": [
    "print(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "bbc58c44-41f7-4af8-bd15-c82f9f4028bf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_list.append(14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "cf150f7c-0f8a-4a63-8691-65c38b46f351",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_list.append('This is a wonderful day')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "5d5cc8a7-66ad-4a9a-8bea-17ed7975933a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_list.append(10>5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "32077d4a-3761-48ed-bad5-89bc74b617f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "print(my_list[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "8806a4e7-736b-4078-bf15-ae1d058cdb45",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "my_list.remove(10>5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "b3121bfa-09ec-458e-9606-3067fc0af633",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "num_int = 145\n",
    "num_flo = 1.45\n",
    "num_new = num_int + num_flo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "cce8a826-c67e-4398-9821-fd24e9fbe5d6",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data type of num_int: <class 'int'>\n",
      "Data type of num_str: <class 'str'>\n",
      "145678\n"
     ]
    }
   ],
   "source": [
    "num_int = 145\n",
    "num_str = '678'\n",
    "print('Data type of num_int:', type(num_int))\n",
    "print('Data type of num_str:', type(num_str))\n",
    "print(str(num_int)+num_str)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "1d129658-f45a-4cb6-bdef-09fbb63610b2",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the 1st number:  56\n",
      "Enter the 2nd number:  78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the sum: 5678\n"
     ]
    }
   ],
   "source": [
    "x = input('Enter the 1st number: ')\n",
    "y = input('Enter the 2nd number: ')\n",
    "print ('Here is the sum:', x+y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "5ac330cb-bf75-48f9-aa48-ef8501d1a34f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the 1st number:  56\n",
      "Enter the 2nd number:  78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the sum: 134\n"
     ]
    }
   ],
   "source": [
    "x = int(input('Enter the 1st number: '))\n",
    "y = int(input('Enter the 2nd number: '))\n",
    "print ('Here is the sum:', x+y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "940c634d-831b-45cf-b347-18ef7be1cc5c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the 1st number:  89\n",
      "Enter the 2nd number:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the sum: 95\n"
     ]
    }
   ],
   "source": [
    "a = input('Enter the 1st number: ')\n",
    "b = input('Enter the 2nd number: ')\n",
    "print ('Here is the sum:', int (a)+int(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "849ed629-8408-43dd-991e-e04ecddf16b1",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the 1st number:  8\n",
      "Enter the 2nd number:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the sum: 17\n"
     ]
    }
   ],
   "source": [
    "a = eval(input('Enter the 1st number: '))\n",
    "b = eval(input('Enter the 2nd number: '))\n",
    "print ('Here is the sum:', a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "268551ff-a2ef-445a-9d7e-558a4f9719f4",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
