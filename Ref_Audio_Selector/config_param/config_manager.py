import configparser
import os
import Ref_Audio_Selector.common.common as common


class ParamReadWriteManager:
    def __init__(self):
        self.base_dir = 'Ref_Audio_Selector/file/base_info'
        self.work_dir = 'work_dir'
        self.role = 'role'
        self.generate_audio_url = 'generate_audio_url'
        self.text_param = 'text_param'
        self.ref_path_param = 'ref_path_param'
        self.ref_text_param = 'ref_text_param'
        self.emotion_param = 'emotion_param'

    def read(self, key):
        file_path = os.path.join(self.base_dir, key + '.txt')
        if os.path.exists(file_path):
            content = common.read_file(file_path)
            return content.strip()
        else:
            return ''

    def write(self, key, content):
        file_path = os.path.join(self.base_dir, key + '.txt')
        clean_content = content.strip()
        common.write_text_to_file(clean_content, file_path)


class ConfigManager:
    def __init__(self):
        self.config_path = 'Ref_Audio_Selector/config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, encoding='utf-8')

    def get_base(self, key):
        return self.config.get('Base', key)

    def get_log(self, key):
        return self.config.get('Log', key)

    def get_audio_sample(self, key):
        return self.config.get('AudioSample', key)

    def get_inference(self, key):
        return self.config.get('Inference', key)

    def get_result_check(self, key):
        return self.config.get('ResultCheck', key)

    def get_audio_config(self, key):
        return self.config.get('AudioConfig', key)

    def get_other(self, key):
        return self.config.get('Other', key)

    def print(self):
        # 打印所有配置
        for section in self.config.sections():
            print('[{}]'.format(section))
            for key in self.config[section]:
                print('{} = {}'.format(key, self.config[section][key]))
            print()


_config = ConfigManager()
_param_read_write_manager = ParamReadWriteManager()


def get_config():
    return _config


def get_rw_param():
    return _param_read_write_manager


if __name__ == '__main__':
    print(_config.print())
