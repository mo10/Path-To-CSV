object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Import CSV to Region'
  ClientHeight = 243
  ClientWidth = 330
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = Form1Create
  DesignSize = (
    330
    243)
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 8
    Top = 8
    Width = 48
    Height = 13
    Caption = 'File list:'
  end
  object btn_add: TButton
    Left = 272
    Top = 160
    Width = 43
    Height = 25
    Anchors = [akRight, akBottom]
    Caption = '+'
    TabOrder = 0
    OnClick = btn_addClick
  end
  object ListView1: TListView
    Left = 8
    Top = 24
    Width = 312
    Height = 126
    Anchors = [akLeft, akTop, akRight, akBottom]
    Columns = <
      item
        AutoSize = True
      end>
    GridLines = True
    MultiSelect = True
    ReadOnly = True
    RowSelect = True
    ShowColumnHeaders = False
    TabOrder = 1
    ViewStyle = vsReport
  end
  object btn_del: TButton
    Left = 208
    Top = 160
    Width = 43
    Height = 25
    Anchors = [akRight, akBottom]
    Caption = '-'
    TabOrder = 2
    OnClick = btn_delClick
  end
  object btn_gen: TButton
    Left = 248
    Top = 208
    Width = 75
    Height = 25
    Anchors = [akRight, akBottom]
    Caption = 'Import'
    TabOrder = 3
    OnClick = btn_genClick
  end
  object OpenDialog1: TOpenDialog
    DefaultExt = '.csv'
    Options = [ofHideReadOnly, ofAllowMultiSelect, ofEnableSizing]
    Title = #36873#25321'csv'#25991#20214
    Left = 16
    Top = 216
  end
end
