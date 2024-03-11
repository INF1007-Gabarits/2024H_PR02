import pygame
import pygame.freetype
from pygame.locals import *
from assets.constants.constants import Constants

# Define additional constants for UI
BUTTON_SPACING = 20  # Space between buttons
BUTTON_MARGIN = 20  # Margin on the right side
BUTTON_WIDTH = 60  # New width for smaller buttons
BUTTON_HEIGHT = 30

# Define the initial selected cell
selected_cell = None

# Define a grid dictionary to store cell values
grid_values = {}


pygame.mixer.init()
pygame.init()

pygame.display.set_caption(Constants.GAME_TITLE)
pygame.display.set_icon(pygame.image.load(Constants.FAVICON))


screen = pygame.display.set_mode(
    [Constants.SCREEN_WIDTH,
     Constants.SCREEN_HEIGHT]
)


def draw_button(screen, image_path, position, title, max_size=(100, 100), font_size=24):
    # Load and scale the button image
    button = pygame.image.load(image_path)
    original_size = button.get_size()
    aspect_ratio = original_size[0] / original_size[1]
    new_width = min(max_size[0], original_size[0])
    new_height = min(max_size[1], original_size[1])

    if original_size[0] > max_size[0] or original_size[1] > max_size[1]:
        if aspect_ratio >= 1:
            new_height = int(new_width / aspect_ratio)
        else:
            new_width = int(new_height * aspect_ratio)

    button = pygame.transform.scale(button, (new_width, new_height))

    # Blit the scaled image
    screen.blit(button, position)

    # Render the button's title
    font = pygame.font.Font(None, font_size)  # None for default font
    text_surf = font.render(title, True, (0, 0, 0))  # Black text
    text_rect = text_surf.get_rect(
        center=(position[0] + new_width // 2, position[1] - new_height // 4))

    # Blit the text onto the screen
    screen.blit(text_surf, text_rect)

    return button.get_rect(topleft=position)


def draw_value(screen, value, position):
    font = pygame.freetype.SysFont("Arial", 24)
    font.render_to(screen, position, str(value), (0, 0, 0))


def splash_screen():
    running = True

    background = pygame.image.load(Constants.SPLASH_SCREEN_BACKGROUND)
    background = pygame.transform.scale(
        background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    screen.blit(background, (0, 0))

    play_button_image = pygame.image.load(Constants.PLAY_BUTTON)
    play_button_size = play_button_image.get_size()
    play_button_scaled = pygame.transform.scale(
        play_button_image, (play_button_size[0] // 1.5, play_button_size[1] // 1.5))
    play_button_rect = play_button_scaled.get_rect(center=(
        Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT - Constants.SCREEN_HEIGHT // 5))
    screen.blit(play_button_scaled, play_button_rect.topleft)

    font_path = pygame.freetype.match_font("Consolas")
    font_size = 80
    font = pygame.freetype.Font(font_path, font_size)
    font_color = (255, 255, 255)
    text_animation_counter = 0
    increase = True

    pygame.mixer.music.load(Constants.MUSIC_PATH)
    pygame.mixer.music.set_volume(Constants.DEFAULT_VOLUME)
    pygame.mixer.music.play(-1)

    while running:
        mouse_pos = pygame.mouse.get_pos()

        if play_button_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN and play_button_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                running = False

        if increase:
            text_animation_counter += 1
            if text_animation_counter > 10:
                increase = False
        else:
            text_animation_counter -= 1
            if text_animation_counter < -10:
                increase = True

        font_size = max(100 + text_animation_counter * 2, 80)
        font.size = font_size
        title_surface, title_rect = font.render("Sudoku", font_color)
        title_rect.center = (Constants.SCREEN_WIDTH // 2,
                             Constants.SCREEN_HEIGHT // 5)

        screen.blit(background, (0, 0))
        screen.blit(play_button_scaled, play_button_rect.topleft)
        screen.blit(title_surface, title_rect)

        pygame.display.flip()
        pygame.time.wait(50)


def draw_sudoku_grid(screen):
    grid_origin = (50, 50)
    grid_size = 450
    cell_size = grid_size // 9
    line_color = (0, 0, 0)

    for i in range(10):
        line_width = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, line_color, (grid_origin[0] + i * cell_size, grid_origin[1]),
                         (grid_origin[0] + i * cell_size, grid_origin[1] + grid_size), line_width)
        pygame.draw.line(screen, line_color, (grid_origin[0], grid_origin[1] + i * cell_size),
                         (grid_origin[0] + grid_size, grid_origin[1] + i * cell_size), line_width)


def draw_sudoku_screen():
    screen.fill((255, 255, 255))

    background = pygame.image.load(Constants.SUDOKU_SCREEN_BACKGROUND)
    background = pygame.transform.scale(
        background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    screen.blit(background, (0, 0))

    hint_button_rect = draw_button(
        screen, Constants.HINT_BUTTON,
        (600, 100), "Indices", max_size=(100, 100)
    )

    refresh_button_rect = draw_button(
        screen, Constants.REFRESH_BUTTON,
        (600, 275), "Nouvelle partie", max_size=(100, 100)
    )

    # Draw difficulty buttons
    difficulty_button_rects = draw_difficulty_buttons(
        screen, 520, 400)

    draw_sudoku_grid(screen)
    draw_numbers_with_fading(screen)

    return refresh_button_rect, hint_button_rect, difficulty_button_rects


def draw_difficulty_buttons(screen, start_x, start_y):
    # Define colors for the difficulty levels
    colors = [(0, 255, 0), (255, 255, 0), (255, 100, 0)]  # Green, Yellow, Red
    titles = ["Facile", "Intermédiaire", "Avancé"]
    rects = []

    x = start_x
    for i, (title, color) in enumerate(zip(titles, colors)):
        # Draw each button with its title and color
        rect = draw_colored_button(
            screen, (x, start_y), title, color, padding=(10, 5))
        rects.append(rect)
        # Increment x for the next button, taking into account the width of the button just drawn and spacing
        x += rect.width + BUTTON_SPACING

    return rects


def draw_colored_button(screen, position, title, color, padding=(10, 5)):
    # Render the button's title
    font = pygame.font.Font(None, 20)  # Adjust font size as needed
    # Black text for visibility
    text_surf = font.render(title, True, (0, 0, 0))
    text_size = text_surf.get_size()

    # Calculate the size of the button with padding
    button_width = text_size[0] + 2 * padding[0]
    button_height = text_size[1] + 2 * padding[1]
    button_size = (button_width, button_height)

    # Create a rectangle
    button_rect = pygame.Rect(position, button_size)
    # Fill the rectangle with the specified color
    pygame.draw.rect(screen, color, button_rect)

    # Get the center of the new rect for positioning the text
    text_rect = text_surf.get_rect(center=button_rect.center)

    # Blit the text onto the screen
    screen.blit(text_surf, text_rect)

    return button_rect


def draw_numbers_with_fading(screen):
    font = pygame.freetype.SysFont("Arial", 24)
    for position, value in grid_values.items():
        alpha = value['alpha']
        if alpha < 255:
            value['alpha'] += 5  # Increase alpha for fading effect
            alpha = min(255, alpha)  # Ensure alpha does not exceed 255

        text_surface, _ = font.render(str(value['number']), (0, 0, 0))
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, position)


def main():
    splash_screen()
    refresh_button_rect, hint_button_rect, difficulty_button_rects = draw_sudoku_screen()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()

        # Change cursor to hand if over any button
        over_any_button = any(rect.collidepoint(mouse_pos) for rect in difficulty_button_rects) or refresh_button_rect.collidepoint(
            mouse_pos) or hint_button_rect.collidepoint(mouse_pos)
        pygame.mouse.set_cursor(
            pygame.SYSTEM_CURSOR_HAND if over_any_button else pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                # Refresh button
                if refresh_button_rect.collidepoint(event.pos):
                    print("Refresh button clicked")
                # Hint button
                elif hint_button_rect.collidepoint(event.pos):
                    print("Hint button clicked")
                # Difficulty buttons
                else:
                    for i, rect in enumerate(difficulty_button_rects):
                        if rect.collidepoint(event.pos):
                            # Identify which difficulty button was clicked
                            if i == 0:
                                print("Easy difficulty selected")
                            elif i == 1:
                                print("Intermediate difficulty selected")
                            elif i == 2:
                                print("Hard difficulty selected")
                            break
            elif event.type == KEYDOWN:
                if event.unicode in '123456789':
                    # Sample action on key press
                    grid_values[(Constants.SCREEN_WIDTH // 2, Constants.SCREEN_HEIGHT // 2)] = {
                        'number': event.unicode,
                        'alpha': 0
                    }

        if not running:
            break

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
