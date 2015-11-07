 {
    'targets' : [
      {
        'target_name': 'test-client',
        'type' : 'executable',

        'includes' : [
            'common.gypi',
        ],

        'include_dirs' : [
            '.',
            './src',
        ],

        'default_configuration': 'Debug',
        'configurations': {
          'Debug': {
            'defines': [ 'DEBUG', '_DEBUG' ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': 1, # static debug
              },
            },
          },
          'Release': {
            'defines': [ 'NDEBUG' ],
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': 0, # static release
              },
            },
          }
        },

        'sources' : [
        	'<(DEPTH)/src/Resource.h',
            '<(DEPTH)/src/SimpleWindow.cpp',
            '<(DEPTH)/src/SimpleWindow.h',
            '<(DEPTH)/src/SimpleWindow.ico',
            '<(DEPTH)/src/SimpleWindow.rc',
            '<(DEPTH)/src/small.ico',
            '<(DEPTH)/src/stdafx.cpp',
            '<(DEPTH)/src/stdafx.h',
            '<(DEPTH)/src/targetver.h',
        ],
        'link_settings': {
            'libraries': [
              '-limm32.lib',
              '-loleacc.lib',
              '-lComdlg32.lib',
              '-lWininet.lib',
              ],
        },
        'msvs_settings' : {
            'VCLinkerTool': {
                'AdditionalDependencies': [
                    'shell32.lib',
                    'kernel32.lib',
                    'user32.lib',
                    'gdi32.lib',
                    'winspool.lib',
                    'comdlg32.lib',
                    'advapi32.lib',
                    'shell32.lib',
                    'ole32.lib',
                    'oleaut32.lib',
                    'uuid.lib',
                    'odbc32.lib',
                    'odbccp32.lib',
                ],
            },
        },
      },
    ],
}
