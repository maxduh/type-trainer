import pygame
import read
import save

def check_if_is_letter(key):
    additional_keys = [1093,1111,1078,1108,1073,1102]
    if key <= 127:
        return True
    else:
        for i in additional_keys:
            if i == key:
                return True
        return False
    
def push_to_text(text , key,text_max_length):
    if len(text) < text_max_length:
        text = text + key
    else:
        text = text[1:text_max_length] + key    
    return text

def show_fps(win, font, clock,fps_history):
    fps_history.append(clock.get_fps())
    if len(fps_history) > 10:
        fps_history.pop(0)
    fps = font.render(str(sum(fps_history)/len(fps_history))[0:6], True, (255, 255, 255))
    win.blit(fps, (10, 10))
    return fps_history

def main():

    width = 1920
    height = 1080
    
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (200, 200, 200)
    WHITE = (255, 255, 255)

    index_end = save.load()

    text = ""
    #text_to_type = "Одного разу, прокинувшись, ти бачиш за вікном вогонь. Ти його не розпалював. Але гасити його доведеться й тобі"
    get_text = read.get_text(index_end)
    text_to_type, index_start, index_end = get_text[0], get_text[1], get_text[2]
    text_max_length = 1000

    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Type Trainer")

    font = pygame.font.Font("RobotoMono-Regular.ttf", 36)

    clock = pygame.time.Clock()
    run = True
    fps_history = []
    while run:
        #pygame.time.delay(100)
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if len(text) == len(text_to_type):
                    save.save(text,text_to_type, index_start, index_end)
                    get_text = read.get_text(index_end)
                    text_to_type, index_start, index_end = get_text[0], get_text[1], get_text[2]
                    text = ""
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(text) < len(text_to_type):
                    text = push_to_text(text, " ", text_max_length)
            elif event.type == pygame.KEYDOWN and check_if_is_letter(event.key):
                if len(text) < len(text_to_type):
                    text = push_to_text(text, str(event.unicode), text_max_length)
                
        
        correct_letters = ""
        wrong_letters = ""

        for i in range(len(text)):
            if i >= len(text_to_type):
                break
            if text[i] == text_to_type[i]:
                correct_letters += text[i]
                wrong_letters += " "
            else:
                if text[i] == " ":
                    wrong_letters += "_"
                else:
                    wrong_letters += text[i]
                correct_letters += " "
        
        img = font.render(correct_letters, True, WHITE)
        if len(text) < len(text_to_type):
            img2 = font.render(text_to_type[len(text)], True, GRAY) 
            img3 = font.render(text_to_type[len(text)+1:], True, GRAY)
            rect2 = img2.get_rect(center=(width/2, height/2))
            rect3 = img3.get_rect(center=(img3.get_width()/2+15+width/2, height/2))
            pygame.draw.rect(win, (55, 55, 55), (width/2-12, height/2-18, 24, 36))
            win.blit(img2, rect2)
            win.blit(img3, rect3)
        img4 = font.render(wrong_letters, True, RED)
        rect = img.get_rect(center=(-img.get_width()/2-15+width/2, height/2))
        
        rect4 = img4.get_rect(center=(-img.get_width()/2-15+width/2, height/2))
        win.blit(img4, rect4)
        win.blit(img, rect)

        
        clock.tick()
        fps_history=show_fps(win, font, clock,fps_history)
        pygame.display.update()

if __name__ == "__main__":
    main()


