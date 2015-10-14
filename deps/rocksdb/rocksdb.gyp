{'targets': [{
    'target_name': 'rocksdb'
  , 'variables': {
        'rdbversion': '4.1.fb'
    }
  , 'type': 'static_library'
		# Overcomes an issue with the linker and thin .a files on SmartOS
  , 'standalone_static_library': 1
  , 'dependencies': [
        '../snappy/snappy.gyp:snappy'
    ]
  , 'direct_dependent_settings': {
        'include_dirs': [
            'rocksdb-<(rdbversion)/include/'
          , 'rocksdb-<(rdbversion)/port/'
          , 'rocksdb-<(rdbversion)/util'
          , 'rocksdb-<(rdbversion)/'
        ]
    }
  , 'defines': [
        'SNAPPY=1'
    ]
  , 'include_dirs': [
        'rocksdb-<(rdbversion)/'
      , 'rocksdb-<(rdbversion)/include/'
    ]
  , 'conditions': [
        ['OS == "win"', {
            'include_dirs': [
                'rocksdb-<(rdbversion)/port/win'
              , 'port-libuv/'
            ]
          , 'defines': [
                'rocksdb_PLATFORM_UV=1'
              , 'NOMINMAX=1'
              , '_HAS_EXCEPTIONS=0'
            ]
          , 'sources': [
                'port-libuv/port_uv.cc'
              , 'port-libuv/env_win.cc'
              , 'port-libuv/win_logger.cc'
            ]
          , 'msvs_settings': {
                'VCCLCompilerTool': {
                    'RuntimeTypeInfo': 'false'
                  , 'EnableFunctionLevelLinking': 'true'
                  , 'ExceptionHandling': '2'
                  , 'DisableSpecificWarnings': [ '4355', '4530' ,'4267', '4244' ]
                }
            }
        }, { # OS != "win"
            'sources': [
                'rocksdb-<(rdbversion)/port/port_posix.cc'
              , 'rocksdb-<(rdbversion)/port/port_posix.h'
              , 'rocksdb-<(rdbversion)/util/env_posix.cc'
            ]
          , 'defines': [
                'rocksdb_PLATFORM_POSIX=1'
            ]
          , 'ccflags': [
                '-fno-builtin-memcmp'
              , '-fPIC'
            ]
          , 'cflags': [ '-std=c++0x' ]
          , 'cflags!': [ '-fno-tree-vrp' ]
        }]
      , ['OS != "win"' and 'OS != "freebsd"', {
            'cflags': [
                '-Wno-sign-compare'
              , '-Wno-unused-but-set-variable'
            ]
        }]
      , ['OS == "linux"', {
            'defines': [
                'OS_LINUX=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "freebsd"', {
            'defines': [
                'OS_FREEBSD=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
          , 'cflags': [
                '-Wno-sign-compare'
            ]
        }]
      , ['OS == "solaris"', {
            'defines': [
                'OS_SOLARIS=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lrt'
              , '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "mac"', {
            'defines': [
                'OS_MACOSX=1'
            ]
          , 'libraries': []
          , 'ccflags': []
          , 'xcode_settings': {
                'WARNING_CFLAGS': [
                    '-Wno-sign-compare'
                  , '-Wno-unused-variable'
                  , '-Wno-unused-function'
                ]
            }
        }]
    ]
  , 'sources': [
        'rocksdb-<(rdbversion)/db/builder.cc'
      , 'rocksdb-<(rdbversion)/db/builder.h'
      , 'rocksdb-<(rdbversion)/db/db_impl.cc'
      , 'rocksdb-<(rdbversion)/db/db_impl.h'
      , 'rocksdb-<(rdbversion)/db/db_iter.cc'
      , 'rocksdb-<(rdbversion)/db/db_iter.h'
      , 'rocksdb-<(rdbversion)/db/filename.cc'
      , 'rocksdb-<(rdbversion)/db/filename.h'
      , 'rocksdb-<(rdbversion)/db/dbformat.cc'
      , 'rocksdb-<(rdbversion)/db/dbformat.h'
      , 'rocksdb-<(rdbversion)/db/rocksdb_main.cc'
      , 'rocksdb-<(rdbversion)/db/log_format.h'
      , 'rocksdb-<(rdbversion)/db/log_reader.cc'
      , 'rocksdb-<(rdbversion)/db/log_reader.h'
      , 'rocksdb-<(rdbversion)/db/log_writer.cc'
      , 'rocksdb-<(rdbversion)/db/log_writer.h'
      , 'rocksdb-<(rdbversion)/db/memtable.cc'
      , 'rocksdb-<(rdbversion)/db/memtable.h'
      , 'rocksdb-<(rdbversion)/db/repair.cc'
      , 'rocksdb-<(rdbversion)/db/skiplist.h'
      , 'rocksdb-<(rdbversion)/db/snapshot.h'
      , 'rocksdb-<(rdbversion)/db/table_cache.cc'
      , 'rocksdb-<(rdbversion)/db/table_cache.h'
      , 'rocksdb-<(rdbversion)/db/version_edit.cc'
      , 'rocksdb-<(rdbversion)/db/version_edit.h'
      , 'rocksdb-<(rdbversion)/db/version_set.cc'
      , 'rocksdb-<(rdbversion)/db/version_set.h'
      , 'rocksdb-<(rdbversion)/db/write_batch.cc'
      , 'rocksdb-<(rdbversion)/db/write_batch_internal.h'
      , 'rocksdb-<(rdbversion)/helpers/memenv/memenv.cc'
      , 'rocksdb-<(rdbversion)/helpers/memenv/memenv.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/cache.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/comparator.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/db.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/dumpfile.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/env.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/filter_policy.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/iterator.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/options.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/slice.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/status.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/table.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/table_builder.h'
      , 'rocksdb-<(rdbversion)/include/rocksdb/write_batch.h'
      , 'rocksdb-<(rdbversion)/port/port.h'
      , 'rocksdb-<(rdbversion)/table/block.cc'
      , 'rocksdb-<(rdbversion)/table/block.h'
      , 'rocksdb-<(rdbversion)/table/block_builder.cc'
      , 'rocksdb-<(rdbversion)/table/block_builder.h'
      , 'rocksdb-<(rdbversion)/table/filter_block.cc'
      , 'rocksdb-<(rdbversion)/table/filter_block.h'
      , 'rocksdb-<(rdbversion)/table/format.cc'
      , 'rocksdb-<(rdbversion)/table/format.h'
      , 'rocksdb-<(rdbversion)/table/iterator.cc'
      , 'rocksdb-<(rdbversion)/table/iterator_wrapper.h'
      , 'rocksdb-<(rdbversion)/table/merger.cc'
      , 'rocksdb-<(rdbversion)/table/merger.h'
      , 'rocksdb-<(rdbversion)/table/table.cc'
      , 'rocksdb-<(rdbversion)/table/table_builder.cc'
      , 'rocksdb-<(rdbversion)/table/two_level_iterator.cc'
      , 'rocksdb-<(rdbversion)/table/two_level_iterator.h'
      , 'rocksdb-<(rdbversion)/util/arena.cc'
      , 'rocksdb-<(rdbversion)/util/arena.h'
      , 'rocksdb-<(rdbversion)/util/bloom.cc'
      , 'rocksdb-<(rdbversion)/util/cache.cc'
      , 'rocksdb-<(rdbversion)/util/coding.cc'
      , 'rocksdb-<(rdbversion)/util/coding.h'
      , 'rocksdb-<(rdbversion)/util/comparator.cc'
      , 'rocksdb-<(rdbversion)/util/crc32c.cc'
      , 'rocksdb-<(rdbversion)/util/crc32c.h'
      , 'rocksdb-<(rdbversion)/util/env.cc'
      , 'rocksdb-<(rdbversion)/util/filter_policy.cc'
      , 'rocksdb-<(rdbversion)/util/hash.cc'
      , 'rocksdb-<(rdbversion)/util/hash.h'
      , 'rocksdb-<(rdbversion)/util/logging.cc'
      , 'rocksdb-<(rdbversion)/util/logging.h'
      , 'rocksdb-<(rdbversion)/util/mutexlock.h'
      , 'rocksdb-<(rdbversion)/util/options.cc'
      , 'rocksdb-<(rdbversion)/util/random.h'
      , 'rocksdb-<(rdbversion)/util/status.cc'
    ]
}]}
