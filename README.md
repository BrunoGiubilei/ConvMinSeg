![Conversor Minutos para Segundos em python](https://github.com/BrunoGiubilei/ConvMinSeg/blob/main/convMinSeg.png)

# ConvSegMin

ConvSegMin é um conversor Python de minutos e segundos para segundos.

## Instalação

Para criar um arquivo .exe a partir deste projeto Python, você pode usar o PyInstaller. Aqui estão os passos básicos:

1. Instale o PyInstaller: Você pode instalar o PyInstaller usando pip, que é o gerenciador de pacotes do Python. Abra o terminal e execute o seguinte comando:
```bash
pip install pyinstaller
```

2. Navegue até o diretório do script: Use o comando cd para navegar até o diretório que contém o script Python (main.py, no seu caso).
3. Crie o arquivo .exe: Agora você pode usar o PyInstaller para criar um arquivo .exe do script. O comando a seguir cria um único arquivo .exe:
```bash
pyinstaller --onefile main.py
```
Após a execução bem-sucedida deste comando, você encontrará o arquivo .exe no diretório dist.

## Execução

Para executar o programa via terminal, você pode usar o seguinte comando:
```bash
python main.py
```
Para executar o programa através de um atalho adicionado na pasta de programas do menu iniciar, você pode criar um  atalho do arquivo main.vbs dentro da pasta 
```bash
C:\Users\{seu_usuario}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
```

## Criação do Setup.exe

Para criar um instalador que crie uma pasta no computador com o .exe dentro e crie atalhos na área de trabalho e no menu, você pode usar o Inno Setup. Aqui estão as etapas básicas:

1. Baixe e instale o Inno Setup.
2. Crie um script de instalação: O Inno Setup usa scripts de instalação, que são arquivos de texto que definem todas as opções de instalação.
3. Defina as opções de instalação: No script de instalação, você pode definir várias opções, como o diretório de instalação, os atalhos do menu Iniciar e da área de trabalho, e muito mais.
4. Compile o script de instalação: Depois de definir todas as opções de instalação, você pode compilar o script de instalação para criar o instalador.

Aqui está um exemplo básico de um script de instalação do Inno Setup:

```bash
[Setup]
AppName=ConvMinSeg
AppVersion=1.0
DefaultDirName={pf}\ConvMinSeg
OutputDir=.
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\workspace\ConvMinSeg\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ConvMinSeg"; Filename: "{app}\main.exe"
Name: "{commondesktop}\ConvMinSeg"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar um ícone na área de trabalho"; GroupDescription: "Atalhos adicionais:"
```