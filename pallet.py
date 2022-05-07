def display_pallet(colors, show_color):
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((40, 10, 60, 30), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((70, 10, 90, 30), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((100, 10, 120, 30), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((130, 10, 150, 30), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((160, 10, 180, 30), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((190, 10, 210, 30), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((220, 10, 240, 30), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((250, 10, 270, 30), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))