import requests
import json
import urllib.request

from utils.config import Config


class Version:
	@staticmethod
	def check():
		page = requests.get("https://api.github.com/repos/Redume/EveryDayPhotoNasa/tags")
		data = json.loads(page.text)
		if Config.get_setting(path="config.ini", section="Settings", setting="version") != data[0]["name"]:
			print("Надено обновление. Перехожу к автоматическому обновлению.")
			Version.download()
		else:
			print("У вас установлена последняя версия.")

	@staticmethod
	def download():
		try:
			version = requests.get("https://api.github.com/repos/Redume/EveryDayPhotoNasa/tags")
			config_version = Config.get_setting(path="config.ini", section="Settings", setting="version")
			data = json.loads(version.text)

			urllib.request.urlretrieve(
				"https://github.com/Redume/EveryDayPhotoNasa/releases/download/" +
				f"{data[0]['name']}/EveryDayPhotoNasa.exe",
				"EveryDayPhotoNasa.exe"
			)

		except urllib.error.HTTPError:
			print("\nНе удалось загрузить обновление.")
		else:
			print(
				"\nОбновление успешно загружено. " +
				f"\n{config_version} => {data[0]['name']}"
			)

			Config.update_setting(path="config.ini", section="Settings", setting="version", value=data[0]['name'])
