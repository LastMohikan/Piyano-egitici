import pygame
import sys
import json
import os

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piyano Eğitici")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 255, 100)
YELLOW = (255, 255, 0)
GRAY = (180, 180, 180)


font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 48)


key_map = {
    'a': 'c1',
    's': 'd1',
    'd': 'e1',
    'f': 'f1',
    'g': 'g1',
    'h': 'a1',
    'j': 'b1'
}


keys = list(key_map.values())
key_rects = []
key_sounds = {}
for i, note in enumerate(keys):
    rect = pygame.Rect(i * 100, 100, 100, 250)
    key_rects.append((rect, note))
    key_sounds[note] = pygame.mixer.Sound(f'sounds/{note}.wav')

pressed_keys = {}


def draw_song_notes(song, current_index, max_visible=8):
    start = max(0, current_note_index - max_visible // 2)
    end = min(len(song), start + max_visible)
    visible_notes = song[start:end]
    for i, note in enumerate(visible_notes):
        color = YELLOW if (start + i) == current_index else GRAY
        text = font.render(note.upper(), True, color)
        x = 30 + i * 90
        y = 30
        screen.blit(text, (x, y))


def show_menu():
    screen.fill(BLACK)
    title = big_font.render("Bir şarkı seçin:", True, WHITE)
    screen.blit(title, (WIDTH // 2 - 120, 50))
    songs = [
        "1 - Twinkle Twinkle",
        "2 - Mary Had a Little Lamb",
        "3 - Jingle Bells"
    ]
    for i, item in enumerate(songs):
        text = font.render(item, True, GRAY)
        screen.blit(text, (WIDTH // 2 - 140, 120 + i * 40))
    pygame.display.flip()

    selected_song = None
    while not selected_song:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_song = 'twinkle'
                elif event.key == pygame.K_2:
                    selected_song = 'mary'
                elif event.key == pygame.K_3:
                    selected_song = 'jingle'
    return selected_song


def load_song(song_name):
    path = os.path.join("songs", f"{song_name}.json")
    with open(path, 'r') as f:
        return json.load(f)


def show_message_and_wait(message):
    screen.fill(BLACK)
    lines = message.split('\n')
    for i, line in enumerate(lines):
        text = big_font.render(line, True, WHITE)
        screen.blit(text, (WIDTH // 2 - 200, 150 + i * 50))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


def run_app(song):
    global current_note_index
    current_note_index = 0
    running = True

    auto_play = False
    AUTO_PLAY_INTERVAL = 700  
    last_play_time = 0
    auto_note_active = None
    auto_note_end_time = 0

    while running:
        screen.fill(BLACK)

        draw_song_notes(song, current_note_index)

        
        for i, (rect, note) in enumerate(key_rects):
            is_pressed = pressed_keys.get(note) or (auto_note_active == note)
            color = GREEN if is_pressed else WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

            key_char = next((k for k, v in key_map.items() if v == note), '')
            label = f"{note.upper()} ({key_char.upper()})"
            label_text = font.render(label, True, BLACK)
            screen.blit(label_text, (rect.x + 10, rect.y + 100))

       
        auto_btn_width, auto_btn_height = 160, 40
        auto_btn_x = WIDTH - auto_btn_width - 20
        auto_btn_y = HEIGHT - auto_btn_height - 20
        auto_btn_rect = pygame.Rect(auto_btn_x, auto_btn_y, auto_btn_width, auto_btn_height)
        pygame.draw.rect(screen, GRAY, auto_btn_rect)
        auto_label = font.render("Otomatik Çal", True, BLACK)
        screen.blit(auto_label, (auto_btn_x + 20, auto_btn_y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                key_name = pygame.key.name(event.key)
                if key_name in key_map:
                    note = key_map[key_name]
                    key_sounds[note].play()
                    pressed_keys[note] = True

                    if note == song[current_note_index]:
                        current_note_index += 1
                        if current_note_index >= len(song):
                            show_message_and_wait("Şarkı tamamlandı!\nMenüye dönmek için bir tuşa basın.")
                            return
                    else:
                        print("Yanlış tuş!")

            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                if key_name in key_map:
                    note = key_map[key_name]
                    pressed_keys[note] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if auto_btn_rect.collidepoint(event.pos):
                    auto_play = not auto_play
                    last_play_time = pygame.time.get_ticks()

        
        if auto_play and current_note_index < len(song):
            now = pygame.time.get_ticks()
            if now - last_play_time >= AUTO_PLAY_INTERVAL:
                note = song[current_note_index]
                key_sounds[note].play()
                auto_note_active = note
                auto_note_end_time = now + 200  
                current_note_index += 1
                last_play_time = now

                if current_note_index >= len(song):
                    show_message_and_wait("Şarkı tamamlandı!\nMenüye dönmek için bir tuşa basın.")
                    return

        
        if auto_note_active and pygame.time.get_ticks() > auto_note_end_time:
            auto_note_active = None



while True:
    selected = show_menu()
    song_data = load_song(selected)
    run_app(song_data)
