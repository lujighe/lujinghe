from tools import my_utils
import glob
import os


class RefAudioListManager:
    def __init__(self, root_dir):
        self.audio_dict = {'default': []}
        absolute_root = os.path.abspath(root_dir)

        for subdir, dirs, files in os.walk(absolute_root):
            relative_path = os.path.relpath(subdir, absolute_root)

            if relative_path == '.':
                category = 'default'
            else:
                category = relative_path.replace(os.sep, '')

            for file in files:
                if file.endswith('.wav'):
                    # 将相对路径转换为绝对路径
                    audio_abs_path = os.path.join(subdir, file)
                    if category not in self.audio_dict:
                        self.audio_dict[category] = []
                    self.audio_dict[category].append(audio_abs_path)

    def get_audio_list(self):
        return self.audio_dict

    def get_flattened_audio_list(self):
        all_audio_files = []
        for category_audios in self.audio_dict.values():
            all_audio_files.extend(category_audios)
        return all_audio_files

    def get_ref_audio_list(self):
        audio_info_list = []
        for category, audio_paths in self.audio_dict.items():
            for audio_path in audio_paths:
                filename_without_extension = os.path.splitext(os.path.basename(audio_path))[0]
                audio_info = {
                    'emotion': f"{category}-{filename_without_extension}",
                    'ref_path': audio_path,
                    'ref_text': filename_without_extension,
                }
                audio_info_list.append(audio_info)
        return audio_info_list


def batch_clean_paths(paths):
    """
    批量处理路径列表，对每个路径调用 clean_path() 函数。

    参数:
        paths (list[str]): 包含待处理路径的列表。

    返回:
        list[str]: 经过 clean_path() 处理后的路径列表。
    """
    cleaned_paths = []
    for path in paths:
        cleaned_paths.append(my_utils.clean_path(path))
    return cleaned_paths


def read_text_file_to_list(file_path):
    # 按照UTF-8编码打开文件（确保能够正确读取中文）
    with open(file_path, mode='r', encoding='utf-8') as file:
        # 读取所有行并存储到一个列表中
        lines = file.read().splitlines()
    return lines


def get_filename_without_extension(file_path):
    """
    Given a file path string, returns the file name without its extension.

    Parameters:
    file_path (str): The full path to the file.

    Returns:
    str: The file name without its extension.
    """
    base_name = os.path.basename(file_path)  # Get the base name (file name with extension)
    file_name, file_extension = os.path.splitext(base_name)  # Split the base name into file name and extension
    return file_name  # Return the file name without extension


def read_file(file_path):
    # 使用with语句打开并读取文件
    with open(file_path, 'r', encoding='utf-8') as file:  # 'r' 表示以读取模式打开文件
        # 一次性读取文件所有内容
        file_content = file.read()

    # 文件在with语句结束时会自动关闭
    # 现在file_content变量中存储了文件的所有文本内容
    return file_content


def write_text_to_file(text, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except IOError as e:
        print(f"Error occurred while writing to the file: {e}")
    else:
        print(f"Text successfully written to file: {output_file_path}")