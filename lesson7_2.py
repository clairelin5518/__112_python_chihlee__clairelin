
import tools

def main():
    while(True):
        tools.playGame()
        playAgain=input('你還要繼續嗎？(y,n)')
        if playAgain=='n':
            break

    print('結束')

if __name__=='__main__':
    main()