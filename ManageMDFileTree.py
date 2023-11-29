#pathlibは別途pipでインストールしておく。
import pathlib
import os
import PySimpleGUI as sg


def main():

    Folderpath = sg.popup_get_folder("フォルダを選択してください")
    if Folderpath == None:
        return
    #Folderpath = os.getcwd()#対象フォルダを指定
    outputpath = 'index.md'#テキストファイルを作成
    f = open(outputpath, mode='w')#テキストファイルを書き込みモードで開く

    output = '```plantuml\n@startuml\ntitle ディレクトリ構成図\nskinparam TitleFontSize 0\n\nsalt\n\n{\n\t{T\n'
    f.write(output)
    #実行ファイルのパスを追加
    subdirname = os.path.basename(str(Folderpath))
    output = '+ ' + str(subdirname) + '\t| [概要を記載]' + '\n'
    
    f.write(output)

    GetFolderFileNames(Folderpath, 0, f)
    output = '\t}\n}\n@enduml\n```'
    f.write(output)


def GetFolderFileNames(path, kaiso, f):
    files = pathlib.Path(path).glob('*')#その階層のフォルダやファイルを取得

    for file in files:
        output = '\t' * (kaiso + 1) + '+' * (kaiso + 2) + ' ' + file.name + '\t| [概要を記載]' + '\n'
        f.write(output)

        if file.is_file() == False:
            GetFolderFileNames(file, kaiso+1, f)

if __name__ == "__main__":
    main()
