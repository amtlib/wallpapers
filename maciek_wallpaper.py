from selenium import webdriver
import os


driver = webdriver.PhantomJS()
driver.set_window_size(1440, 900)
driver.get('http://koziejka.github.io/wall')
driver.save_screenshot('maciek_wallpaper')


os.system('gsettings set org.gnome.desktop.background draw-background false && gsettings set org.gnome.desktop.background picture-uri file://{}/{}'.format(os.path.dirname(os.path.abspath(__file__)), 'maciek_wallpaper'))
