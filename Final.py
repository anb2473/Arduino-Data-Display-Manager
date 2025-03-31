# for reading serial data
import serial
# for handling screen
import pygame as pg
# for handling JSON data
import json
# for handling file states
import os
# for CSV recording
import datetime
# for handling socket connection
import socket

import threading

# for cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

import json

import os

import RenderMethods

pg.init()



def multiply_list(mult_list, val):
    # multiply each value in the list
    result = [x * val for x in mult_list]
    return result


def add_lists(list1, list2):
    # zip lists and add each value
    result = [x + y for x, y in zip(list1, list2)]
    return result


def meter(self, param, info):
    # prepare icon
    image = pg.image.load(info['ico']) if isinstance(info['ico'], str) else info['ico']
    image = pg.transform.scale(image,
                               (info['size'][0] / info['ico-size'][0], info['size'][1] / info['ico-size'][1]))
    info['ico'] = image

    rect = image.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + self.offset,
                                  info['pos'][1] + info['size'][1] / 2 - info['size'][1] / 5))

    screen_rect = pg.rect.Rect((0, 0), (pg.display.get_surface().get_size()))

    if screen_rect.contains(rect):
        self.display.blit(image, rect)

        # prepare bar (background)
        rect = pg.Rect(info['pos'][0] + info['size'][0] / 10 + self.offset,
                       info['pos'][1] + info['size'][1] / 2 + info['size'][1] / 16,
                       info['size'][0] / 1.25,
                       info['size'][1] / 6)
        pg.draw.rect(self.display, info['bar-color'], rect, border_radius=10)

        if info.get('offset') is not None and self.data.get(param) is not None:
            val = float(self.data.get(param)) + info['offset']
        else:
            val = self.data.get(param)
        if val is not None:
            # calculate color
            high = multiply_list(info['high'], min(max(int(255 * float(val)) / info['max'], 0), 255))
            low = multiply_list(info['low'], min(max(255 - int(255 * float(val) / info['max']), 0), 255))
            color = add_lists(high, low)
            # render bar (foreground)
            rect = pg.Rect(info['pos'][0] + info['size'][0] / 10 + self.offset,
                           info['pos'][1] + info['size'][1] / 2 + info['size'][1] / 16,
                           max(min(info['size'][0] / 1.25 * (float(val) * info['multiplex']) / info['max'],
                                   info['size'][0] / 1.25), 0),
                           info['size'][1] / 6)
            pg.draw.rect(self.display, color, rect, border_radius=10)

        # render data
        surf = self.font.render(
            f'{val}{info['ext'].replace('{DEG}', chr(176))}' if self.data.get(param) is not None
            else 'NO DATA',
            False, 'white')
        rect = surf.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + self.offset,
                                     info['pos'][1] + info['size'][1] / 2 + info['size'][1] / 3))
        self.display.blit(surf, rect)

    return info


def vert_meter(self, param, info):
    # prepare icon
    image = pg.image.load(info['ico']) if isinstance(info['ico'], str) else info['ico']
    image = pg.transform.scale(image,
                               (info['size'][0] / info['ico-size'][0], info['size'][1] / info['ico-size'][1]))
    info['ico'] = image

    rect = image.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + self.offset,
                                  info['pos'][1] + info['size'][1] / 2 - info['size'][1] / 3.5))

    screen_rect = pg.rect.Rect((0, 0), (pg.display.get_surface().get_size()))

    if screen_rect.contains(rect):
        self.display.blit(image, rect)

        # render bar (background)
        rect = pg.Rect(info['pos'][0] + info['size'][0] / 3.75 + info['size'][0] / 16 + self.offset,
                       info['pos'][1] + info['size'][1] / 2.8,
                       info['size'][0] / 3,
                       info['size'][1] / 2.5)
        pg.draw.rect(self.display, info['bar-color'], rect, border_radius=10)

        if info.get('offset') is not None and self.data.get(param) is not None:
            val = float(self.data.get(param)) + info['offset']
        else:
            val = self.data.get(param)
        if val is not None:
            # calculate color
            high = multiply_list(info['high'], min(max(int(255 * float(val)) / info['max'], 0), 255))
            low = multiply_list(info['low'], min(max(255 - int(255 * float(val) / info['max']), 0), 255))
            color = add_lists(high, low)
            # render bar
            rect = pg.Rect(info['pos'][0] + info['size'][0] / 3.75 + info['size'][0] / 16 + self.offset,
                           info['pos'][1] + (info['size'][1] / 1.3 - max(
                               min(info['size'][1] / 2.5 * (float(val) * info['multiplex']) / info['max'],
                                   info['size'][1] / 2.5), 0)),
                           info['size'][0] / 3,
                           max(min(info['size'][1] / 2.5 * (float(val) * info['multiplex']) / info['max'],
                                   info['size'][1] / 2.5), 0))
            pg.draw.rect(self.display, color, rect, border_radius=10)

        # render text data
        surf = self.font.render(
            f'{val}{info['ext'].replace('{DEG}', chr(176))}' if val is not None
            else 'NO DATA',
            False, 'white')
        rect = surf.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + self.offset,
                                     info['pos'][1] + info['size'][1] / 2 + info['size'][1] / 3))
        self.display.blit(surf, rect)

    return info


def graph(self, param, info):
    # prepare icon
    image = pg.image.load(info['ico']) if isinstance(info['ico'], str) else info['ico']
    image = pg.transform.scale(image,
                               (info['size'][0] / info['ico-size'][0], info['size'][1] / info['ico-size'][1]))
    info['ico'] = image

    rect = image.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + info['ico-offset'][0] + self.offset,
                                  info['pos'][1] + info['size'][1] / 2 - info['size'][1] / 5 + info['ico-offset'][
                                      1]))

    screen_rect = pg.rect.Rect((0, 0), (pg.display.get_surface().get_size()))

    if screen_rect.contains(rect):
        self.display.blit(image, rect)

        # render text data
        surf = self.font.render(
            f'{self.data.get(param)}{info['ext'].replace('{DEG}', chr(176))}' if self.data.get(param) is not None
            else 'NO DATA',
            False, 'white')
        rect = surf.get_rect(center=(info['pos'][0] + info['size'][0] / 2 + self.offset,
                                     info['pos'][1] + info['size'][1] / 2 + info['size'][1] / 3))
        self.display.blit(surf, rect)

        # prepare points
        if info.get('points') is None:
            info['points'] = []

        # insert point
        if info.get('offset') is not None and self.data.get(param) is not None:
            val = float(self.data.get(param)) + info['offset']
        else:
            val = self.data.get(param)
        if val is not None: info['points'].append(int(float(val)))
        # minimize points
        if len(info['points']) > info['max-points']:
            info['points'] = info['points'][1:]

        # prepare bar (background)
        rect = pg.Rect(info['pos'][0] + info['size'][0] / 20 + self.offset, info['pos'][1] + info['size'][1] / 2.6,
                       info['size'][0] / 1.1, info['size'][1] / 3)
        pg.draw.rect(self.display, info['bar-color'], rect, border_radius=10)

        # setup render variables
        width = (info['size'][0] / 1.2 / info['max-points'])
        index = 0
        prev_loc = None
        for point in info['points']:
            if prev_loc is None:
                # render entry point
                pg.draw.circle(self.display, info['line-color'], ((info['pos'][0] + info['size'][0] / 12) + self.offset,
                                                                  info['pos'][1] + (info['size'][1] / 1.5)
                                                                  - info['size'][1] / 4 * min(point, info['max-val'])
                                                                  / info['max-val']), 3)
            else:
                # render line segment
                pg.draw.line(self.display, info['line-color'], prev_loc,
                             ((info['pos'][0] + info['size'][0] / 12) + (width * index) + self.offset,
                              info['pos'][1] + (info['size'][1] / 1.5)
                              - info['size'][1] / 4 * min(point, info['max-val'])
                              / info['max-val']), 5)
            # calculate previous loc
            prev_loc = (info['pos'][0] + info['size'][0] / 12 + width * index + self.offset,
                        info['pos'][1] + (info['size'][1] / 1.5)
                        - info['size'][1] / 4 * min(point, info['max-val'])
                        / info['max-val'])
            index += 1

    return info



def brighten(color, incr):
    new_color = []
    for value in color:
        new_color.append(min(value + incr, 255))
    return new_color


def dashed_line(surf, start, end, color):
    num_of_dashes = round((end[1] - start[1]) / 15)
    for i in range(num_of_dashes):
        print()
        end_y = start[1] + i * 15 + 10 if start[1] + i * 15 + 10 <= end[1] else end[1]
        pg.draw.line(surf, color, (start[0], start[1] + i * 15), (start[0], end_y), 3)


class Visualizer:
    def __init__(self, display=None):
        self.shiftdelay = 0
        if display is None:
            pg.display.set_mode((1000, 750), pg.RESIZABLE)
            self.display = pg.display.get_surface()
        else:
            self.display = display
            self.shiftdelay = 50
        pg.display.set_caption('Visualizer')
        pg.display.set_icon(pg.image.load('resources/ico.png'))

        self.csv = {}
        self.open_csv = ''
        self.open_csv_name = ''

        self.offset = 0

        self.csv_active = False
        self.csv_val = ''

        self.visualizer_active = False
        self.activation_delay = 0

        self.font = pg.font.Font(None, 35)
        self.small_font = pg.font.Font(None, 20)

        self.mouse = pg.math.Vector2()
        self.offset_scroll = 0

        self.visualizer_surf = pg.Surface((800, 600))
        self.visualizer_surf.fill((20, 20, 20))

        self.max_length = 0
        self.max_val = 0

        self.cutinstance = False

        self.side_screen_value = '   NO FILES OPEN'

        with open('run.json', 'r') as f:
            self.run_data = json.load(f)
            self.set_csvs = self.run_data['csv']
            self.config = self.run_data['config']
            self.colors = self.run_data['csv-colors']

        self.possible_items = self.set_csvs

        for f in self.set_csvs:
            if os.path.exists(f'csv/{f}.csv'):
                with open(f'csv/{f}.csv', 'r') as file:
                    lines = file.readlines()
                    self.csv[f] = [line.split(',') if not line.startswith('#') else line for line in lines[1:]]

    def render_text(self, text, loc, color):
        surf = self.font.render(text, False, color)
        self.display.blit(surf, loc)

    def prepare(self):
        self.display.fill((20, 20, 20))

    def draw_gradient_rect(self, rect, top_color, bottom_color, vert=True):
        x, y, width, height = rect
        gradient_surf = pg.Surface((width, height), pg.SRCALPHA)
        for i in range(height):
            if vert:
                alpha = 255 * (1 - i / height)
            else:
                alpha = 255 * (i / height)
            color = top_color.lerp(bottom_color, i / height)
            color.a = int(alpha)
            pg.draw.line(gradient_surf, color, (0, i), (width, i))
        self.display.blit(gradient_surf, (x, y))

    def render(self):
        click_counted = False

        self.prepare()

        if not self.visualizer_active:
            index = 0
            for line in self.open_csv:
                if 135 + index * 50 - self.offset_scroll > self.display.get_height():
                    break
                if type(line) is str:
                    if 135 + index * 50 - self.offset_scroll > 100: self.render_text(line.strip(), (
                        70 + self.offset, 135 + index * 50 - self.offset_scroll), (0, 200, 150))
                else:
                    width = 0
                    for i in range(len(line)):
                        if 135 + index * 50 - self.offset_scroll > 100:
                            self.render_text(line[i].strip(),
                                             (width + 70 + self.offset, 135 + index * 50 - self.offset_scroll),
                                             self.config['csv-colors'][i])
                        width += self.font.size(line[i])[0] + self.config['csv-split']
                index += 1

            cover_rect = pg.Rect(0, 100, self.display.get_width(), 10)
            pg.draw.rect(self.display, (20, 20, 20), cover_rect)

            cover_rect = pg.Rect(0, 110, self.display.get_width(), 25)
            self.draw_gradient_rect(cover_rect, pg.Color(20, 20, 20, 255), pg.Color(20, 20, 20, 0))

            cover_rect = pg.Rect(0, self.display.get_height() - 25, self.display.get_width(), 25)
            self.draw_gradient_rect(cover_rect, pg.Color(20, 20, 20, 0), pg.Color(20, 20, 20, 255), vert=False)
        else:
            self.display.blit(self.visualizer_surf, (self.offset + 50, 175))

        surf = self.font.render(self.side_screen_value[3:], False,
                                'red' if self.side_screen_value.startswith('ERR') else 'white')
        self.side_screen_rect = surf.get_rect(topright=(self.display.get_width() - 75 - self.offset, 75))
        self.display.blit(surf, self.side_screen_rect)

        self.offset = (self.display.get_width() - 1000) / 2

        rect = pg.Rect(355 + self.offset, 65, 50, 40)
        color = (60, 60, 60)
        if self.visualizer_active:
            color = (125, 125, 125)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            if not self.visualizer_active:
                color = (100, 100, 100)
            if self.activation_delay <= 0 and pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or \
                    pg.mouse.get_pressed()[2]:
                self.visualizer_active = not self.visualizer_active
                self.activation_delay = 300
        self.activation_delay -= 1
        pg.draw.rect(self.display, color, rect, border_radius=10)

        self.render_text('V', (372 + self.offset, 75), 'white')

        rect = pg.Rect(425 + self.offset, 65, 50, 40)
        color = (60, 60, 60)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            color = (100, 100, 100)
            if self.open_csv != '' and self.activation_delay <= 0 and pg.mouse.get_pressed()[0] or \
                    pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                # noinspection PyBroadException
                try:
                    self.csv.pop(self.open_csv_name)
                    self.open_csv = []
                    self.visualizer_surf.fill((20, 20, 20))
                    if os.path.exists(f'csv/{self.open_csv_name}.csv'): os.remove(f'csv/{self.open_csv_name}.csv')
                except:
                    pass

        self.activation_delay -= 1
        pg.draw.rect(self.display, color, rect, border_radius=10)

        self.render_text('C', (442 + self.offset, 75), 'white')

        rect = pg.Rect(55 + self.offset, 65, 275, 40)
        color = (60, 60, 60)
        if self.csv_active:
            color = (75, 75, 75)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            color = (100, 100, 100)
            if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                click_counted = True
                self.csv_active = True
        if len(self.possible_items) == 0 or not self.csv_active:
            pg.draw.rect(self.display, color, rect, border_radius=10)
        else:
            pg.draw.rect(self.display, color, rect, border_top_left_radius=10, border_top_right_radius=10)

        if self.csv_active:
            rect = pg.Rect(self.font.size(f'{self.csv_val}')[0] + 78 + self.offset, 75, 13, 22)
            pg.draw.rect(self.display, "white", rect)

            index = 0
            for item in self.possible_items:
                rect = pg.Rect(55 + self.offset, 105 + 40 * index, 275, 40)
                color = (60, 60, 60)
                if self.csv_active:
                    color = (75, 75, 75)
                if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
                    color = (100, 100, 100)
                    if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                        click_counted = True
                        self.csv_active = False
                        self.csv_val = item
                        self.load_file()
                        self.search_csv()
                if index + 1 == len(self.possible_items):
                    pg.draw.rect(self.display, color, rect, border_bottom_left_radius=10, border_bottom_right_radius=10)
                else:
                    pg.draw.rect(self.display, color, rect)

                self.render_text(item, (65 + self.offset, 110 + 40 * index), 'white')
                index += 1

        self.render_text(self.csv_val, (70 + self.offset, 75), 'white')
        self.render_text('CSV', (70 + self.offset, 35), 'white')

        color = (60, 60, 60)
        rect = pg.rect.Rect(-50 + self.offset, 65, 50, 40)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            if (pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]) and self.shiftdelay < 0:
                # subapp = Manager(display=self.display)
                # subapp.start()
                self.cutinstance = True
            color = (100, 100, 100)
        pg.draw.rect(self.display, color, rect, border_radius=10)

        self.render_text(text=f'M', loc=(-35 + self.offset, 75), color='white')

        if not click_counted and pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
            self.csv_active = False

        pg.display.update()

    def manage_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                self.manage_key(key=event.key, unicode=event.unicode)

    def load_file(self):
        try:
            self.open_csv_name = self.csv_val

            self.offset_scroll = 0
            self.open_csv = self.csv[self.csv_val]
            data_entry = self.config['display-data']

            # noinspection PyBroadException
            try:
                multiplex = self.config[self.csv_val + ' multiplex']
            except:
                multiplex = 1

            self.max_length = 0
            for item in self.open_csv:
                self.max_length += 1
                if len(item) >= data_entry and item[data_entry] != ' ':
                    val = int(float(item[data_entry].strip().split(' ')[0]) * multiplex)
                    if val > self.max_val:
                        self.max_val = val

            write_file = True

            try:
                index = 0
                prev_point = None
                norm_width = 800 / self.max_length
                norm_height = 500 / self.max_val
                prev_date = ''
                prev_x = -10000000
                prev_width = 0
                self.visualizer_surf.fill((20, 20, 20))
                for item in self.open_csv:
                    if item[0] == '#':
                        prev_point = None
                        if item.startswith('# ---- N'):
                            val = item.split(',')[1].strip().split(' ')[0]
                            if val != prev_date:
                                prev_date = val
                                surf = self.small_font.render(val, False, 'white')
                                width = surf.get_width()
                                x = 100 + index * norm_width - width / 2
                                if x - width / 2 > prev_x - prev_width / 2:
                                    self.visualizer_surf.blit(surf, (x, 515))
                                    prev_x = x
                                    prev_width = width
                    elif len(item) >= data_entry:
                        if item[data_entry] != ' ':
                            val = int(float(item[data_entry].strip().split(' ')[0]) * multiplex)

                            if prev_point is None:
                                dashed_line(self.visualizer_surf,
                                                 (100 + index * norm_width, 500 - norm_height * val),
                                                 (100 + index * norm_width, 500),
                                                 brighten(self.colors[self.csv_val], 50))
                            else:
                                pg.draw.line(self.visualizer_surf, self.colors[self.csv_val], prev_point,
                                             (100 + index * norm_width, 500 - norm_height * val), 5)
                            prev_point = (100 + index * norm_width, 500 - norm_height * val)

                            index += 1
            except Exception as e:
                print(e)
                write_file = False
                self.side_screen_value = 'ERRVISUALIZATION ERROR'

            self.max_length *= 50
            self.max_length -= 550

            if write_file:
                self.side_screen_value = f'   FILE={self.csv_val}'
        except Exception as e:
            print(e)
            self.side_screen_value = 'ERRFILE NOT FOUND'

    def search_csv(self):
        new_items = []
        for item in self.possible_items:
            if item.startswith(self.csv_val):
                new_items.append(item)
        self.possible_items = new_items

    def manage_key(self, key, unicode):
        if key == pg.K_RETURN:
            self.load_file()
        elif self.csv_active:
            if key == pg.K_BACKSPACE:
                self.csv_val = self.csv_val[:-1]
                new_items = []
                for item in self.set_csvs:
                    if item.startswith(self.csv_val):
                        new_items.append(item)
                self.possible_items = new_items
            elif self.font.size(f'{self.csv_val}')[0] < 225:
                self.csv_val += unicode
                self.search_csv()

    def manage_scroll(self):
        if not self.visualizer_active:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                self.csv_active = False
                if self.offset_scroll > 0:
                    self.offset_scroll -= 10
            elif keys[pg.K_DOWN]:
                self.csv_active = False
                if self.offset_scroll < self.max_length:
                    self.offset_scroll += 10

    def run(self):
        while not self.cutinstance:
            try:
                self.shiftdelay -= 1
                self.render()

                self.manage_events()
                self.manage_scroll()

                self.mouse = pg.mouse.get_pos()
            except Exception as e:
                print(f'CRITICAL ERROR: {e}')

        del self


def multiply_list(mult_list, val):
    # multiply each value in the list
    result = [x * val for x in mult_list]
    return result


def add_lists(list1, list2):
    # zip lists and add each value
    result = [x + y for x, y in zip(list1, list2)]
    return result


def encrypt(aesgcm, message, nonce):
    # use AESGCM to encrypt data
    return aesgcm.encrypt(nonce, message.encode(), None)


def decrypt(aesgcm, message, nonce):
    # use AESGCM to decrypt data
    return aesgcm.decrypt(nonce, message, None)


class Manager:
    def __init__(self):
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Generate public key
        self.public_key = self.private_key.public_key()

        self.public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # initiate pygame
        pg.init()

        # access JSON data as dict type
        with open('run.json', 'r') as f:
            self.run_data = json.load(f)

        # opem dict branches
        self.app_info = self.run_data['data']
        self.cvs = self.run_data['csv']
        self.config = self.run_data['config']

        # set up CSV delay
        self.csv_delay = self.config['csv-timeout']
        self.active_csv_delay = self.csv_delay

        # prepare files
        for f in self.cvs:
            # generate file
            if not os.path.exists(f'csv/{f}.csv'):
                with open(f'csv/{f}.csv', 'w') as file:
                    file.write(f'{self.cvs[f]}\n')
            # build entry
            with open(f'csv/{f}.csv', 'a') as file:
                file.write(f'# ---- New Entry, {datetime.datetime.now()} ---- #\n')

        # setup pygame display
        self.shiftdelay = 0

        pg.display.set_mode((1000, 750), pg.RESIZABLE)
        self.display = pg.display.get_surface()

        self.offset = 0
        pg.display.set_caption('Tank Manager')
        pg.display.set_icon(pg.image.load('resources/ico.png'))

        # build font
        self.font = pg.font.Font(None, 35)

        self.data = {}

        # setup connection data
        self.arduino = None
        self.remote = False
        self.locked = False
        self.baud = '9600'
        self.port = 'COM'
        self.password = ''

        # setup side screen data
        self.side_screen_data = 'ERRNO CONNECTION'
        self.side_screen_rect = pg.Rect(0, 0, 0, 0)

        # setup bool locators
        self.port_active = False
        self.baud_active = False
        self.password_active = False

        # setup mouse data
        self.delay = 200
        self.mouse = pg.math.Vector2()

        # setup encryption
        self.cipher = None

        self.cutinstance = False

    def connect(self):
        # noinspection PyBroadException
        try:
            if self.baud.__contains__('.'):
                # noinspection PyBroadException
                try:
                    # connect to server
                    self.remote = True
                    self.arduino = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.arduino.connect((self.baud, int(self.port)))
                    self.locked = True
                    self.side_screen_data = f'   CONNECTED'
                except:
                    # error program
                    self.arduino = None
                    self.side_screen_data = 'ERRSOCKET CONNECTION ERROR'
            else:
                # open serial connection
                self.remote = False
                self.arduino = serial.Serial(port=self.port, baudrate=int(self.baud), timeout=.1)
                self.side_screen_data = f'   CONNECTED'
            for f in self.cvs:
                # insert connection data to CSV
                with open(f'csv/{f}.csv', 'a') as file:
                    file.write(f'# ---- Connection Opened, Port={self.port} Baud={self.baud} ---- #\n')
        except:
            self.side_screen_data = 'ERRCOM CONNECTION ERROR'

    def write_read(self):
        if self.remote:
            if not self.locked:
                # access data and decrypt
                data = self.cipher.decrypt(self.arduino.recv(1024)).decode()
                # key = self.cipher.decrypt(self.arduino.recv(1024)).decode()
                # self.cipher = Fernet(key)
            else: data = ''
        else: data = self.arduino.readline().decode()
        return data

    def manage_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # safely quit program
                pg.quit()
                if self.arduino:
                    self.arduino.close()
                exit()
            elif event.type == pg.KEYDOWN:
                self.manage_key(key=event.key, unicode=event.unicode)

    def manage_key(self, key, unicode):
        if key == pg.K_RETURN:
            if self.password_active:
                # noinspection PyBroadException
                try:
                    # attempt to validate connection and pass keys
                    self.arduino.send(self.public_key_pem)
                    self.arduino.settimeout(3)
                    encrypted_symmetric_key = self.arduino.recv(1024)

                    symmetric_key = self.private_key.decrypt(
                        encrypted_symmetric_key,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )

                    nonce = os.urandom(12)
                    aesgcm = AESGCM(symmetric_key)

                    self.arduino.send(encrypt(aesgcm, self.password, nonce))
                    self.arduino.send(nonce)

                    # noinspection PyBroadException
                    try:
                        ret = self.arduino.recv(1024)
                        ret = decrypt(aesgcm, ret, nonce)
                        self.cipher = Fernet(ret)
                        self.locked = False
                    except:
                        self.arduino = None
                        self.side_screen_data = 'ERRAUTHENTICATION ERROR'
                except:
                    self.side_screen_data = 'ERRSOCKET CONNECTION ERROR'
            else: self.connect()
            if not self.side_screen_data.startswith('ERR'):
                self.port_active = False
                self.baud_active = False
                self.password_active = False
        elif self.port_active:
            if key == pg.K_BACKSPACE:
                self.port = self.port[:-1]
            elif self.font.size(f'{self.port}')[0] < 125:
                self.port += unicode
        elif self.baud_active:
            if key == pg.K_BACKSPACE:
                self.baud = self.baud[:-1]
            elif self.font.size(f'{self.baud}')[0] < 225:
                self.baud += unicode
        elif self.password_active:
            if key == pg.K_BACKSPACE:
                self.password = self.password[:-1]
            elif self.font.size(f'{len(self.password) * '*'}')[0] < 125:
                self.password += unicode

    def render_text(self, text, loc):
        # ALIAS
        surf = self.font.render(text, False, 'white')
        self.display.blit(surf, loc)

    def prepare(self):
        # ALIAS
        self.display.fill((20, 20, 20))

    def render(self):
        # calculate offset
        self.offset = (self.display.get_width() - 1000) / 2

        click_counted = False

        if self.arduino:
            if self.locked:
                # render locked state
                color = (60, 60, 60)
                if self.baud_active:
                    color = (75, 75, 75)
                rect = pg.Rect(55 + self.offset, 165, 175, 40)
                if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
                    if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                        click_counted = True
                        self.port_active = False
                        self.baud_active = False
                        self.password_active = True
                    color = (100, 100, 100)
                pg.draw.rect(self.display, color, rect, border_radius=10)

                # render password
                if self.password_active:
                    rect = pg.Rect(self.font.size(f'{len(self.password) * '*'}')[0] + 78 + self.offset, 175, 13, 22)
                    pg.draw.rect(self.display, "white", rect)
                self.render_text(text=f'{len(self.password) * '*'}', loc=(75 + self.offset, 175))
                self.render_text(text='Password', loc=(70 + self.offset, 135))
            else:
                for param in self.app_info:
                    # render each json widget
                    info = self.app_info[param]

                    rect = pg.Rect(info['pos'][0] + self.offset, info['pos'][1], info['size'][0], info['size'][1])
                    color = info['background-color']
                    if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
                        color = info['hover-color']
                    pg.draw.rect(self.display, color, rect, border_radius=10)

                    info = getattr(RenderMethods, info['visual'])(self, param, info)

                    if info.get('csv_delay') is None:
                        info['csv_delay'] = self.csv_delay
                    info['csv_delay'] -= 1
                    if info['csv_delay'] <= 0:
                        info['csv_delay'] = self.csv_delay
                        if self.data.get(param) is not None:
                            with open(f'csv/{info['csv']}.csv', 'a') as file:
                                file.write(
                                    f'{str(datetime.datetime.now())},{f'{self.data.get(param)}'
                                                                      f'{info['ext'].replace('{DEG}', chr(176))}'}\n')

                    self.app_info[param] = info

        # render side screen data
        surf = self.font.render(self.side_screen_data[3:], False,
                                'red' if self.side_screen_data.startswith('ERR') else 'white')
        self.side_screen_rect = surf.get_rect(topright=(self.display.get_width() - 75 - self.offset, 75))
        self.display.blit(surf, self.side_screen_rect)

        # render port background
        rect = pg.Rect(55 + self.offset, 65, 175, 40)
        color = (60, 60, 60)
        if self.port_active:
            color = (75, 75, 75)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                click_counted = True
                self.port_active = True
                self.baud_active = False
                self.password_active = False
            color = (100, 100, 100)
        pg.draw.rect(self.display, color, rect, border_radius=10)

        # render interactable layer
        if self.port_active:
            rect = pg.Rect(self.font.size(f'{self.port}')[0] + 78 + self.offset, 75, 13, 22)
            pg.draw.rect(self.display, "white", rect)
        self.render_text(text=f'{self.port}', loc=(75 + self.offset, 75))
        self.render_text(text='Port', loc=(70 + self.offset, 35))

        # render baud background
        color = (60, 60, 60)
        if self.baud_active:
            color = (75, 75, 75)
        rect = pg.Rect(250 + self.offset, 65, 275, 40)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                click_counted = True
                self.port_active = False
                self.baud_active = True
                self.password_active = False
            color = (100, 100, 100)
        pg.draw.rect(self.display, color, rect, border_radius=10)

        # render baud interactable layer
        if self.baud_active:
            rect = pg.Rect(self.font.size(f'{self.baud}')[0] + 278 + self.offset, 75, 13, 22)
            pg.draw.rect(self.display, "white", rect)
        self.render_text(text=f'{self.baud}', loc=(275 + self.offset, 75))
        self.render_text(text='Baud/IP', loc=(265 + self.offset, 35))

        # handle mouse input
        if not click_counted and pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
            self.port_active = False
            self.baud_active = False
            self.password_active = False

        color = (60, 60, 60)
        rect = pg.rect.Rect(-50 + self.offset, 65, 50, 40)
        if rect.contains(pg.Rect(self.mouse[0], self.mouse[1], 1, 1)):
            if (pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]) and self.shiftdelay < 0:
                subapp = Visualizer(display=self.display)
                subapp.run()
                self.shiftdelay = 200
            color = (100, 100, 100)
        pg.draw.rect(self.display, color, rect, border_radius=10)

        self.render_text(text=f'V', loc=(-35 + self.offset, 75))

        # update display
        pg.display.update()

    def run(self):
        while not self.cutinstance:
            try:
                self.shiftdelay -= 1

                # prepare display
                self.prepare()

                # noinspection PyBroadException
                try:
                    # read data
                    value: str = self.write_read()
                    if '\r\n' in value:
                        # split data
                        located = {}
                        list_items = value.split('\r\n')
                        list_items.reverse()
                        for item in list_items:
                            # check if item handled
                            if located.get(item[0:3]):
                                break
                            # insert data
                            located[item[0:3]] = True
                            if item[3:] != '':
                                self.data[item[0:3]] = item[3:]
                    else:
                        # insert data
                        self.data[value[0:3]] = value[3:-2]
                except:
                    pass

                # handle events
                self.manage_events()
                # render screen
                self.render()

                # get mouse position
                self.mouse = pg.mouse.get_pos()
            except Exception as e:
                print(f"CRITICAL ERROR: {e}")


if __name__ == '__main__':
    # create instance of Manager and run
    app = Manager()
    app.run()
