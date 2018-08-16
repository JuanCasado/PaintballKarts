import pygame


class Ui:
    def __init__(self, full=True):
        pygame.init()
        pygame.font.init()
        self._full = full
        pygame.display.set_caption("Color Queue")
        pygame.display.set_icon(pygame.image.load("../media/icon.png"))
        pygame.mouse.set_cursor(*pygame.cursors.ball)
        if full:
            self._time_compressor = 50
            self._screen = pygame.display.set_mode((1280, 800), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWACCEL)
        else:
            self._time_compressor = 350
            self._screen = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.RESIZABLE)
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill((250, 250, 200))
        self._background.convert()
        self._clock = pygame.time.Clock()
        self._mainLoop = True
        self._FPS = 60
        self._screen.blit(self._background, (0, 0))
        self.color_picker = ColorPiker(self)
        self.buffer_displayer = BufferDisplayer(self)
        self.ui = (pygame.sprite.Group(),)
        self.desc = Text("F - Full Screen.      M - Minimize.", 0, 0, 0, (0, 0, 0), self.ui, 0)
        self.desc.prepare_to_animate(self.color_picker.background_x,
                                     self.buffer_displayer.background_y + self.buffer_displayer.background_h
                                     - Text.height(self.desc.text, 30),
                                     30)
        self.state = Text("State:", 0, 0, 0, (0, 0, 0), self.ui, 0)
        self.state.prepare_to_animate(self.color_picker.background_x, self.buffer_displayer.background_y, 30)
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_pressed = True
        self.mouse_new = False

    def run(self):
        while self._mainLoop:
            t = self._clock.tick(self._FPS) / self._time_compressor
            self._event_handling()
            self.color_picker.clear(self._screen, self._background)
            self.buffer_displayer.clear(self._screen, self._background)
            for group in self.ui:
                group.clear(self._screen, self._background)
            self.color_picker.update(t, self.mouse_new, self.mouse_pressed, self.mouse_x, self.mouse_y)
            self.buffer_displayer.update(t, self.mouse_new, self.mouse_pressed, self.mouse_x, self.mouse_y)
            self.desc.update(t)
            for group in self.ui:
                group.update(t)
            self.color_picker.draw(self._screen)
            self.buffer_displayer.draw(self._screen)
            for group in self.ui:
                group.draw(self._screen)
            self.mouse_new = False
            pygame.display.flip()
        pygame.font.quit()
        pygame.quit()

    def _event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._mainLoop = False
                elif event.key == pygame.K_f:
                    if not self._full:
                        self._screen = pygame.display.set_mode((1280, 800),
                                                               pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWACCEL)
                        self._background = pygame.Surface(self._screen.get_size())
                        self._background.fill((250, 250, 200))
                        self._background.convert()
                        self._screen.blit(self._background, (0, 0))
                        self._time_compressor = 50
                        self._full = True
                elif event.key == pygame.K_m:
                    if self._full:
                        self._screen = pygame.display.set_mode((1280, 800),
                                                               pygame.DOUBLEBUF | pygame.HWACCEL | pygame.RESIZABLE)
                        self._background = pygame.Surface(self._screen.get_size())
                        self._background.fill((250, 250, 200))
                        self._background.convert()
                        self._screen.blit(self._background, (0, 0))
                        self._time_compressor = 250
                        self._full = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_x = event.pos[0]
                    self.mouse_y = event.pos[1]
                    self.mouse_pressed = True
                    self.mouse_new = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_x = event.pos[0]
                    self.mouse_y = event.pos[1]
                    self.mouse_pressed = False
                    self.mouse_new = True

    def get_w(self):
        return self._screen.get_size()[0]

    def get_h(self):
        return self._screen.get_size()[1]

    def blit(self, surface, pos):
        self._screen.blit(surface, pos)


class Stack:
    pass


class ColorPiker:
    def __init__(self, ui):
        self.background_final_w = ui.get_w() / 2
        self.background_final_h = ui.get_h() / 2
        self.background_x = ui.get_w() / 2 - self.background_final_w / 2 - ui.get_w() / 6
        self.background_y = ui.get_h() / 2 - self.background_final_h / 2
        button_final_w = self.background_final_w / 5
        button_final_h = self.background_final_w / 5
        button_final_y = self.background_final_h / 2 - self.background_final_w / 10 + self.background_y
        button_final_1 = self.background_final_w / 10 + self.background_x
        button_final_2 = self.background_final_w / 5 * 2 + self.background_x
        button_final_3 = self.background_final_w / 5 * 3 + self.background_final_w / 10 + self.background_x
        self.color_1 = (240, 150, 100)
        self.color_2 = (180, 110, 180)
        self.color_3 = (50, 150, 200)
        self.group = (pygame.sprite.LayeredUpdates(),)
        self.background = Box(0, 0, 0, 0, (180, 240, 150), self.group, 0)
        self.background.prepare_to_animate(self.background_x, self.background_y,
                                           self.background_final_w, self.background_final_h)
        self.btt_1 = Box(0, 0, 0, 0, self.color_1, self.group, 1)
        self.btt_1.prepare_to_animate(button_final_1, button_final_y, button_final_w, button_final_h)
        self.btt_2 = Box(0, 0, 0, 0, self.color_2, self.group, 1)
        self.btt_2.prepare_to_animate(button_final_2, button_final_y, button_final_w, button_final_h)
        self.btt_3 = Box(0, 0, 0, 0, self.color_3, self.group, 1)
        self.btt_3.prepare_to_animate(button_final_3, button_final_y, button_final_w, button_final_h)
        self.desc = Text("Click to send.", 0, 0, 0, (0, 0, 0), self.group, 1)
        self.desc.prepare_to_animate(button_final_1, self.background_y + self.background_final_h / 10, 30)
        self._color_timer = 0
        self._color_timer_to_do = False

    def clear(self, screen, background):
        for group in self.group:
            group.clear(screen, background)

    def update(self, t, mouse_new, mouse_pressed, mouse_x, mouse_y):
        if self._color_timer > 0:
            self._color_timer -= 1
        else:
            if self._color_timer_to_do:
                self.btt_1.color = self.color_1
                self.btt_2.color = self.color_2
                self.btt_3.color = self.color_3
                self._color_timer_to_do = False
        if mouse_new and self.background.rect.collidepoint(mouse_x, mouse_y):
            if self.btt_1.rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed:
                    self.btt_1.color = (255, 255, 255)
                    self._color_timer = 30
                    self._color_timer_to_do = True
                else:
                    pass
            elif self.btt_2.rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed:
                    self.btt_2.color = (255, 255, 255)
                    self._color_timer = 30
                    self._color_timer_to_do = True
                else:
                    pass
            elif self.btt_3.rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed:
                    self.btt_3.color = (255, 255, 255)
                    self._color_timer = 30
                    self._color_timer_to_do = True
                else:
                    pass
        for group in self.group:
            group.update(t)

    def draw(self, screen):
        for group in self.group:
            group.draw(screen)


class BufferDisplayer:
    def __init__(self, ui):
        self.group = (pygame.sprite.LayeredUpdates(),)
        self.background_x = ui.get_w() / 2 + ui.get_w() / 6
        self.background_y = ui.get_h() / 4 - ui.get_h() / 8
        self.background_w = ui.get_w() / 4
        self.background_h = ui.get_h() / 2 + ui.get_h() / 4
        self.background = Box(0, 0, 0, 0, (150, 230, 130), self.group, 0)
        self.background.prepare_to_animate(self.background_x, self.background_y, self.background_w, self.background_h)
        self.bucket_tl = Box(0, 0, 0, 0, (80, 30, 30), self.group, 1)
        self.bucket_tl.prepare_to_animate(self.background_x + self.background_w / 6,
                                          self.background_y + self.background_h / 4,
                                          self.background_w / 6,
                                          self.background_h / 40)
        self.bucket_tr = Box(0, 0, 0, 0, (80, 30, 30), self.group, 1)
        self.bucket_tr.prepare_to_animate(self.background_x + self.background_w * 2 / 3,
                                          self.background_y + self.background_h / 4,
                                          self.background_w / 6,
                                          self.background_h / 40)
        self.bucket_bl = Box(0, 0, 0, 0, (80, 30, 30), self.group, 1)
        self.bucket_bl.prepare_to_animate(self.background_x + self.background_w / 3 - self.background_h / 40,
                                          self.background_y + self.background_h / 4,
                                          self.background_h / 40,
                                          self.background_h / 2)
        self.bucket_tl = Box(0, 0, 0, 0, (80, 30, 30), self.group, 1)
        self.bucket_tl.prepare_to_animate(self.background_x + self.background_w * 2 / 3,
                                          self.background_y + self.background_h / 4,
                                          self.background_h / 40,
                                          self.background_h / 2)
        self.bucket_bb = Box(0, 0, 0, 0, (80, 30, 30), self.group, 1)
        self.bucket_bb.prepare_to_animate(self.background_x + self.background_w / 3 - self.background_h / 40,
                                          self.background_y + self.background_h / 4 + self.background_h / 2,
                                          self.background_w / 3 + self.background_h / 20,
                                          self.background_h / 40)
        self.cantidad = Text("Size: ", 0, 0, 0, (0, 0, 0), self.group, 1)
        self.cantidad.prepare_to_animate(self.background_x + self.background_w / 7,
                                         self.background_y + self.background_h / 3 +
                                         self.background_h / 2 + self.background_h / 30,
                                         30)
        self.desc = Text("Click to collect.", 0, 0, 0, (0, 0, 0), self.group, 1)
        self.desc.prepare_to_animate(self.background_x + self.background_w / 2 -
                                     self.desc.width(self.desc.text, 30) / 2,
                                     self.background_y + self.background_h / 14,
                                     30)

    def add(self, color):
        pass

    def clear(self, screen, background):
        for group in self.group:
            group.clear(screen, background)

    def update(self, t, mouse_new, mouse_pressed, mouse_x, mouse_y):
        if mouse_new and self.background.rect.collidepoint(mouse_x, mouse_y):
            pass
        for group in self.group:
            group.update(t)

    def draw(self, screen):
        for group in self.group:
            group.draw(screen)


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color, groups, layer):
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, groups)
        self.rect = pygame.Rect(x, y, w, h)
        self._x = Animator(x, x, 3)
        self._y = Animator(y, y, 3)
        self._w = Animator(w, w, 3)
        self._h = Animator(h, h, 3)
        self._animate = False

        self.color = color
        self.image = pygame.Surface((0, 0))

    def prepare_to_animate(self, x_final, y_final, w_final, h_final):
        self._x.fin = x_final
        self._y.fin = y_final
        self._w.fin = w_final
        self._h.fin = h_final
        self._animate = True

    def update(self, t):
        if self._animate:
            animation_left = False
            self._x.update(t)
            self.rect.x = int(round(self._x.actual, 0))
            animation_left |= self._x.animation_left
            self._y.update(t)
            self.rect.y = int(round(self._y.actual, 0))
            animation_left |= self._y.animation_left
            self._w.update(t)
            self.rect.w = int(round(self._w.actual, 0))
            animation_left |= self._w.animation_left
            self._h.update(t)
            self.rect.h = int(round(self._h.actual, 0))
            animation_left |= self._h.animation_left
            if not animation_left:
                self._animate = False
            err_t = abs(self._x.err + self._y.err + self._w.err + self._h.err)
            if err_t > 120:
                err_t = 120
            err_t = err_t * -180 / 120 + 180
            trans_color = self.color + (err_t,)
            self.image = pygame.Surface((abs(self.rect.width), abs(self.rect.height)), pygame.SRCALPHA)
            self.image.fill(trans_color)
            self.image.convert()
        else:
            self.image = pygame.Surface((self.rect.width, self.rect.height))
            self.image.fill(self.color)
            self.image.convert()


class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, t, color, groups, layer):
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, groups)
        self._x = Animator(x, x, 3)
        self._y = Animator(y, y, 3)
        self._t = Animator(t, t, 100)
        self.color = color
        self._animate = False
        self.text = text
        self.font = pygame.font.SysFont("Impact", t)
        self.image = self.font.render(self.text, True, self.color)
        self.image = self.image.convert_alpha()
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def prepare_to_animate(self, x, y, t):
        self._x.fin = x
        self._y.fin = y
        self._t.fin = t
        self._animate = True

    def update(self, t):
        if self._animate:
            animation_left = False
            self._x.update(t)
            self.rect.x = int(round(self._x.actual, 0))
            animation_left |= self._x.animation_left
            self._y.update(t)
            self.rect.y = int(round(self._y.actual, 0))
            animation_left |= self._y.animation_left
            self._t.update(t)
            animation_left |= self._t.animation_left
            if not animation_left:
                self._animate = False
            err_t = abs(self._x.err + self._y.err + self._t.err)
            if err_t > 200:
                err_t = 200
            elif err_t < 0:
                err_t = 0
            trans_color = (err_t, err_t, err_t,)
            self.font = pygame.font.SysFont("Impact", int(round(self._t.actual, 0)))
            self.image = self.font.render(self.text, True, trans_color)
            self.image = self.image.convert_alpha()
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()
        else:
            self.font = pygame.font.SysFont("Impact", int(round(self._t.actual, 0)))
            self.image = self.font.render(self.text, True, self.color)
            self.image = self.image.convert_alpha()
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()

    @staticmethod
    def width(txt, size):
        return pygame.font.SysFont("Impact", size).size(txt)[0]

    @staticmethod
    def height(txt, size):
        return pygame.font.SysFont("Impact", size).size(txt)[1]


class Animator:
    def __init__(self, inicio, fin, coeficiente):
        self._coeficiente = coeficiente
        self._integral = 0
        self._var_integral_1 = 0
        self._var_integral_2 = 0
        if inicio < fin:
            self._var_integral_1 = 20
            self._var_integral_2 = 1
        else:
            self._var_integral_1 = 1
            self._var_integral_2 = 20
        self.animation_left = False
        self.actual = inicio
        self.fin = fin
        self.err = 0

    def update(self, t):
        self.err = (self.fin - self.actual) / self._coeficiente
        if self.err > 0:
            self._integral += self._var_integral_1
        elif self.err < 0:
            self._integral -= self._var_integral_2
        if (abs(self.err)) > 1:
            self.actual += (self.err + self._integral) * t
        else:
            self.actual = self.fin
        self.animation_left = (self.actual != self.fin)


if __name__ == "__main__":
    a = Ui(False)
    a.run()

