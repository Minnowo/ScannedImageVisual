from PIL import Image

print("enter file name or paste directory")
filename = input()
im = Image.open(filename)
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

number = 99999

for i in range(img.size[0]):
    for j in range(img.size[1]):
        rgb = pixelMap[i,j]
        finalrgb = pixelMap[i,j]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        
        dyer = 75
        dyeg = 75
        dyeb = 75
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 64
        dyeg = 64
        dyeb = 64
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 52
        dyeg = 52
        dyeb = 52
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 39
        dyeb = 39
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 37
        dyeg = 22
        dyeb = 16
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 31
        dyeg = 18
        dyeb = 13
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 26
        dyeg = 15
        dyeb = 11
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 19
        dyeg = 11
        dyeb = 8
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 25
        dyeg = 25
        dyeb = 25
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 21
        dyeg = 21
        dyeb = 21
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 17
        dyeg = 17
        dyeb = 17
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 13
        dyeg = 13
        dyeb = 13
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 86
        dyeg = 91
        dyeb = 91
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 74
        dyeg = 78
        dyeb = 78
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 60
        dyeg = 63
        dyeb = 63
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 45
        dyeg = 47
        dyeb = 47
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 111
        dyeg = 111
        dyeb = 111
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 95
        dyeg = 95
        dyeb = 95
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 78
        dyeb = 78
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 58
        dyeg = 58
        dyeb = 58
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 151
        dyeg = 151
        dyeb = 151
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 130
        dyeg = 130
        dyeb = 130
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 107
        dyeg = 107
        dyeb = 107
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 80
        dyeg = 80
        dyeb = 80
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 165
        dyeg = 165
        dyeb = 165
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 142
        dyeg = 142
        dyeb = 142
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 116
        dyeg = 116
        dyeb = 116
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 87
        dyeg = 87
        dyeb = 87
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 197
        dyeg = 197
        dyeb = 197
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 169
        dyeg = 169
        dyeb = 169
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 138
        dyeg = 138
        dyeb = 138
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 104
        dyeg = 104
        dyeb = 104
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 252
        dyeg = 249
        dyeb = 242
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 217
        dyeg = 214
        dyeb = 208
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 178
        dyeg = 175
        dyeb = 170
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 133
        dyeg = 131
        dyeb = 127
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 252
        dyeg = 252
        dyeb = 252
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 217
        dyeg = 217
        dyeb = 217
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 178
        dyeg = 178
        dyeb = 178
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 133
        dyeg = 133
        dyeb = 133
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 162
        dyeg = 166
        dyeb = 182
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 139
        dyeg = 142
        dyeb = 156
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 114
        dyeg = 117
        dyeb = 127
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 85
        dyeg = 87
        dyeb = 96
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 252
        dyeg = 0
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 217
        dyeg = 0
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 178
        dyeg = 0
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 133
        dyeg = 0
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 101
        dyeg = 125
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 87
        dyeg = 108
        dyeb = 43
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 71
        dyeg = 88
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 53
        dyeg = 66
        dyeb = 27
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 101
        dyeg = 75
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 87
        dyeg = 64
        dyeb = 43
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 71
        dyeg = 52
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 53
        dyeg = 39
        dyeb = 27
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 50
        dyeg = 75
        dyeb = 175
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 43
        dyeg = 64
        dyeb = 151
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 36
        dyeg = 52
        dyeb = 123
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 27
        dyeg = 39
        dyeb = 93
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 125
        dyeg = 62
        dyeb = 175
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 108
        dyeg = 53
        dyeb = 151
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 88
        dyeg = 43
        dyeb = 123
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 66
        dyeg = 33
        dyeb = 93
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 75
        dyeg = 125
        dyeb = 151
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 64
        dyeg = 108
        dyeb = 130
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 52
        dyeg = 88
        dyeb = 106
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 66
        dyeb = 80
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 239
        dyeg = 125
        dyeb = 162
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 206
        dyeg = 108
        dyeb = 140
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 168
        dyeg = 88
        dyeb = 114
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 126
        dyeg = 66
        dyeb = 86
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 125
        dyeg = 202
        dyeb = 25
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 108
        dyeg = 174
        dyeb = 21
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 88
        dyeg = 142
        dyeb = 17
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 66
        dyeg = 107
        dyeb = 13
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 225
        dyeg = 225
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 195
        dyeg = 195
        dyeb = 43
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 159
        dyeg = 159
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 120
        dyeg = 120
        dyeb = 27
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 101
        dyeg = 151
        dyeb = 213
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 87
        dyeg = 130
        dyeb = 183
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 71
        dyeg = 107
        dyeb = 150
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 53
        dyeg = 80
        dyeb = 112
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 176
        dyeg = 75
        dyeb = 213
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 151
        dyeg = 64
        dyeb = 183
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 124
        dyeg = 52
        dyeb = 150
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 93
        dyeg = 39
        dyeb = 112
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 213
        dyeg = 125
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 184
        dyeg = 108
        dyeb = 43
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 150
        dyeg = 88
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 113
        dyeg = 66
        dyeb = 27
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 244
        dyeg = 230
        dyeb = 160
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 210
        dyeg = 199
        dyeb = 138
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 172
        dyeg = 162
        dyeb = 113
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 128
        dyeg = 122
        dyeb = 85
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 149
        dyeg = 108
        dyeb = 76
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 128
        dyeg = 93
        dyeb = 65
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 105
        dyeg = 75
        dyeb = 53
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 56
        dyeb = 39
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 111
        dyeg = 2
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 95
        dyeg = 1
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 1
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 58
        dyeg = 1
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 91
        dyeg = 216
        dyeb = 210
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 186
        dyeb = 180
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 63
        dyeg = 152
        dyeb = 148
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 47
        dyeg = 114
        dyeb = 110
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 125
        dyeg = 176
        dyeb = 55
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 108
        dyeg = 151
        dyeb = 47
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 88
        dyeg = 124
        dyeb = 38
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 66
        dyeg = 93
        dyeb = 29
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 247
        dyeg = 235
        dyeb = 76
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 212
        dyeg = 203
        dyeb = 65
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 174
        dyeg = 166
        dyeb = 53
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 130
        dyeg = 125
        dyeb = 39
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 158
        dyeg = 158
        dyeb = 251
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 136
        dyeg = 136
        dyeb = 217
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 111
        dyeg = 111
        dyeb = 177
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 83
        dyeg = 83
        dyeb = 133
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 0
        dyeg = 123
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 105
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 86
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 64
        dyeb = 0
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 63
        dyeg = 63
        dyeb = 251
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 5
        dyeg = 54
        dyeb = 217
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 44
        dyeg = 44
        dyeb = 177
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 33
        dyeg = 33
        dyeb = 133
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 141
        dyeg = 118
        dyeb = 71
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 122
        dyeg = 101
        dyeb = 61
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 99
        dyeg = 83
        dyeb = 49
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 74
        dyeg = 62
        dyeb = 37
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 151
        dyeg = 50
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 130
        dyeg = 43
        dyeb = 43
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 107
        dyeg = 36
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 80
        dyeg = 27
        dyeb = 27
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 73
        dyeg = 126
        dyeb = 251
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 62
        dyeg = 109
        dyeb = 217
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 51
        dyeg = 89
        dyeb = 117
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 66
        dyeb = 133
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 0
        dyeg = 214
        dyeb = 57
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 185
        dyeb = 49
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 151
        dyeb = 39
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 0
        dyeg = 113
        dyeb = 30
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 127
        dyeg = 85
        dyeb = 48
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 110
        dyeg = 73
        dyeb = 41
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 90
        dyeg = 59
        dyeb = 33
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 67
        dyeg = 44
        dyeb = 25
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 207
        dyeg = 175
        dyeb = 158
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 178
        dyeg = 150
        dyeb = 136
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 145
        dyeg = 123
        dyeb = 111
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 109
        dyeg = 92
        dyeb = 84
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 157
        dyeg = 81
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 135
        dyeg = 69
        dyeb = 31
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 111
        dyeg = 56
        dyeb = 25
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 83
        dyeg = 42
        dyeb = 19
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 147
        dyeg = 86
        dyeb = 106
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 126
        dyeg = 74
        dyeb = 92
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 104
        dyeg = 60
        dyeb = 75
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 77
        dyeg = 45
        dyeb = 56
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 111
        dyeg = 107
        dyeb = 136
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 95
        dyeg = 92
        dyeb = 117
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 75
        dyeb = 95
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 58
        dyeg = 56
        dyeb = 72
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 184
        dyeg = 131
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 158
        dyeg = 113
        dyeb = 31
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 129
        dyeg = 92
        dyeb = 25
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 97
        dyeg = 69
        dyeb = 19
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 102
        dyeg = 116
        dyeb = 52
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 87
        dyeg = 99
        dyeb = 44
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 71
        dyeg = 81
        dyeb = 36
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 53
        dyeg = 60
        dyeb = 28
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 158
        dyeg = 76
        dyeb = 77
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 136
        dyeg = 65
        dyeb = 66
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 111
        dyeg = 53
        dyeb = 54
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 84
        dyeg = 39
        dyeb = 40
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 56
        dyeg = 40
        dyeb = 34
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 48
        dyeg = 35
        dyeb = 30
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 28
        dyeb = 24
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 30
        dyeg = 21
        dyeb = 18
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 133
        dyeg = 106
        dyeb = 96
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 115
        dyeg = 91
        dyeb = 83
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 94
        dyeg = 74
        dyeb = 68
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 70
        dyeg = 55
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 121
        dyeg = 72
        dyeb = 87
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 104
        dyeg = 61
        dyeb = 74
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 85
        dyeg = 50
        dyeb = 61
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 63
        dyeg = 38
        dyeb = 45
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 75
        dyeg = 61
        dyeb = 91
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 64
        dyeg = 52
        dyeb = 78
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 52
        dyeg = 42
        dyeb = 63
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 32
        dyeb = 47
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 75
        dyeg = 49
        dyeb = 34
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 64
        dyeg = 42
        dyeb = 30
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 52
        dyeg = 35
        dyeb = 24
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 26
        dyeb = 18
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 75
        dyeg = 81
        dyeb = 41
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 64
        dyeg = 69
        dyeb = 35
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 52
        dyeg = 56
        dyeb = 29
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 42
        dyeb = 22
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 140
        dyeg = 59
        dyeb = 45
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 121
        dyeg = 50
        dyeb = 38
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 99
        dyeg = 41
        dyeb = 31
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 74
        dyeg = 31
        dyeb = 24
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 20
        dyeg = 178
        dyeb = 129
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 17
        dyeg = 153
        dyeb = 111
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 14
        dyeg = 125
        dyeb = 90
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 10
        dyeg = 94
        dyeb = 68
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 57
        dyeg = 140
        dyeb = 136
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 49
        dyeg = 121
        dyeb = 117
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 39
        dyeg = 99
        dyeb = 95
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 30
        dyeg = 74
        dyeb = 72
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 85
        dyeg = 43
        dyeb = 60
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 73
        dyeg = 37
        dyeb = 51
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 59
        dyeg = 31
        dyeb = 42
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 44
        dyeg = 23
        dyeb = 31
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 22
        dyeg = 125
        dyeb = 130
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 18
        dyeg = 107
        dyeb = 112
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 15
        dyeg = 87
        dyeb = 91
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 11
        dyeg = 65
        dyeb = 68
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 146
        dyeg = 62
        dyeb = 94
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 125
        dyeg = 53
        dyeb = 81
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 103
        dyeg = 43
        dyeb = 66
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 77
        dyeg = 33
        dyeb = 50
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 91
        dyeg = 25
        dyeb = 28
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 78
        dyeg = 21
        dyeb = 24
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 63
        dyeg = 17
        dyeb = 19
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 47
        dyeg = 13
        dyeb = 15
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]


        
        dyer = 187
        dyeg = 47
        dyeb = 48
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 161
        dyeg = 40
        dyeb = 41
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 131
        dyeg = 33
        dyeb = 33
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]
        dyer = 99
        dyeg = 25
        dyeb = 24
        tempr = abs(r - dyer)
        tempg = abs(g - dyeg)
        tempb = abs(b - dyeb)
        tempnum = tempr + tempg + tempb
        if(tempnum < number):
            number = tempnum
            finalrgb = [dyer,dyeg,dyeb]






        pixelsNew[i,j] = (finalrgb[0],finalrgb[1],finalrgb[2],255)
        number = 99999
#print("press any key to close the window...\n")
print("enter name for file")
name = input()
im.close()
img.save(name + ".png")
img.close()