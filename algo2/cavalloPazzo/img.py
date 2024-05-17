from PIL import Image, ImageDraw

def make_img_from_board(vett,n,dimCas,nomeFile):
    img = Image.new('RGB', (n*dimCas, n*dimCas), color = 'white')
    d = ImageDraw.Draw(img)
    cnt = 0
    for cas in vett:
        if cas==1:
            x = (cnt%n)*dimCas
            y = (cnt//n)*dimCas
            d.rectangle([(x,y), (x+dimCas,y+dimCas)], fill='blue')
        cnt+=1
    img.save('./algo2/cavalloPazzo/img/'+str(n)+'/'+nomeFile+'.png')
    return 


if __name__=="__main__":
    num = 5
    #board = [0]*(num*num)
    board = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    make_img_from_board(board,5,1000,'prova1')