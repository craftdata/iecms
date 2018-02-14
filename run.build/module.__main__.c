/* Generated code for Python source for module '__main__'
 * created by Nuitka version 0.5.28.1
 *
 * This code is in part copyright 2017 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The _module___main__ is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The module constants used, if any. */
static PyObject *const_str_plain_run;
static PyObject *const_str_digest_c4bd0fe01abe0c8902f3278a47db0dea;
static PyObject *const_str_plain___package__;
static PyObject *const_str_plain___spec__;
static PyObject *const_str_plain_sys;
static PyObject *const_str_plain_debug;
static PyObject *const_tuple_str_plain_app_tuple;
static PyObject *const_str_plain_host;
static PyObject *const_str_plain_port;
extern PyObject *const_str_plain___file__;
extern PyObject *const_int_0;
extern PyObject *const_str_plain_site;
extern PyObject *const_str_plain_types;
static PyObject *const_str_digest_dadff6dd3651f30e8cbbdd26cdbce215;
static PyObject *const_str_plain_os;
static PyObject *const_dict_7fb9f6337f7279e2616a973f96b3d41f;
static PyObject *const_str_angle_module;
extern PyObject *const_tuple_empty;
static PyObject *const_int_pos_9090;
extern PyObject *const_str_plain___loader__;
extern PyObject *const_str_plain___main__;
static PyObject *const_str_plain___annotations__;
static PyObject *const_str_plain_app;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain___cached__;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_run = UNSTREAM_STRING( &constant_bin[ 0 ], 3, 1 );
    const_str_digest_c4bd0fe01abe0c8902f3278a47db0dea = UNSTREAM_STRING( &constant_bin[ 3 ], 42, 0 );
    const_str_plain___package__ = UNSTREAM_STRING( &constant_bin[ 45 ], 11, 1 );
    const_str_plain___spec__ = UNSTREAM_STRING( &constant_bin[ 56 ], 8, 1 );
    const_str_plain_sys = UNSTREAM_STRING( &constant_bin[ 64 ], 3, 1 );
    const_str_plain_debug = UNSTREAM_STRING( &constant_bin[ 67 ], 5, 1 );
    const_tuple_str_plain_app_tuple = PyTuple_New( 1 );
    const_str_plain_app = UNSTREAM_STRING( &constant_bin[ 72 ], 3, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_app_tuple, 0, const_str_plain_app ); Py_INCREF( const_str_plain_app );
    const_str_plain_host = UNSTREAM_STRING( &constant_bin[ 75 ], 4, 1 );
    const_str_plain_port = UNSTREAM_STRING( &constant_bin[ 79 ], 4, 1 );
    const_str_digest_dadff6dd3651f30e8cbbdd26cdbce215 = UNSTREAM_STRING( &constant_bin[ 83 ], 7, 0 );
    const_str_plain_os = UNSTREAM_STRING( &constant_bin[ 76 ], 2, 1 );
    const_dict_7fb9f6337f7279e2616a973f96b3d41f = _PyDict_NewPresized( 3 );
    PyDict_SetItem( const_dict_7fb9f6337f7279e2616a973f96b3d41f, const_str_plain_host, const_str_digest_dadff6dd3651f30e8cbbdd26cdbce215 );
    const_int_pos_9090 = PyLong_FromUnsignedLong( 9090ul );
    PyDict_SetItem( const_dict_7fb9f6337f7279e2616a973f96b3d41f, const_str_plain_port, const_int_pos_9090 );
    PyDict_SetItem( const_dict_7fb9f6337f7279e2616a973f96b3d41f, const_str_plain_debug, Py_True );
    assert( PyDict_Size( const_dict_7fb9f6337f7279e2616a973f96b3d41f ) == 3 );
    const_str_angle_module = UNSTREAM_STRING( &constant_bin[ 90 ], 8, 0 );
    const_str_plain___annotations__ = UNSTREAM_STRING( &constant_bin[ 98 ], 15, 1 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_1b652b4e81dbb43643af3b231195f18b;
/* For use in "MainProgram.c". */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void)
{
    module_filename_obj = const_str_digest_c4bd0fe01abe0c8902f3278a47db0dea;
    codeobj_1b652b4e81dbb43643af3b231195f18b = MAKE_CODEOBJ( module_filename_obj, const_str_angle_module, 1, const_tuple_empty, 0, 0, CO_NOFREE );
    codeobj_main = codeobj_1b652b4e81dbb43643af3b231195f18b;
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif
#if PYTHON_VERSION >= 330
extern PyObject *const_str_plain___loader__;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
extern void _initCompiledAsyncgenTypes();
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();
#if PYTHON_VERSION >= 350
    _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
    _initCompiledAsyncgenTypes();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = MODULE_DICT( module___main__ );

    CHECK_OBJECT( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if ( GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__, value );
    }

#if PYTHON_VERSION >= 330
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_called_name_1;
    PyObject *tmp_fromlist_name_5;
    PyObject *tmp_globals_name_5;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_kw_name_1;
    PyObject *tmp_level_name_1;
    PyObject *tmp_level_name_2;
    PyObject *tmp_level_name_3;
    PyObject *tmp_level_name_4;
    PyObject *tmp_level_name_5;
    PyObject *tmp_locals_name_5;
    PyObject *tmp_name_name_1;
    PyObject *tmp_name_name_2;
    PyObject *tmp_name_name_3;
    PyObject *tmp_name_name_4;
    PyObject *tmp_name_name_5;
    PyObject *tmp_source_name_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    struct Nuitka_FrameObject *frame_1b652b4e81dbb43643af3b231195f18b;

    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;

    // Module code.
    // Frame without reuse.
    frame_1b652b4e81dbb43643af3b231195f18b = MAKE_MODULE_FRAME( codeobj_1b652b4e81dbb43643af3b231195f18b, module___main__ );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_1b652b4e81dbb43643af3b231195f18b );
    assert( Py_REFCNT( frame_1b652b4e81dbb43643af3b231195f18b ) == 2 );

    // Framed code:
    tmp_name_name_1 = const_str_plain_os;
    tmp_level_name_1 = const_int_0;
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_1, NULL, NULL, NULL, tmp_level_name_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_name_name_2 = const_str_plain_sys;
    tmp_level_name_2 = const_int_0;
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_2, NULL, NULL, NULL, tmp_level_name_2 );
    assert( tmp_unused != NULL );
    Py_DECREF( tmp_unused );
    tmp_name_name_3 = const_str_plain_types;
    tmp_level_name_3 = const_int_0;
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_3, NULL, NULL, NULL, tmp_level_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_name_name_4 = const_str_plain_site;
    tmp_level_name_4 = const_int_0;
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_4, NULL, NULL, NULL, tmp_level_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_c4bd0fe01abe0c8902f3278a47db0dea;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = metapath_based_loader;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___loader__, tmp_assign_source_3 );
    tmp_assign_source_4 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, tmp_assign_source_4 );
    tmp_assign_source_5 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___cached__, tmp_assign_source_5 );
    tmp_assign_source_6 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___package__, tmp_assign_source_6 );
    tmp_assign_source_7 = PyDict_New();
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___annotations__, tmp_assign_source_7 );
    tmp_name_name_5 = const_str_plain_app;
    tmp_globals_name_5 = (PyObject *)moduledict___main__;
    tmp_locals_name_5 = Py_None;
    tmp_fromlist_name_5 = const_tuple_str_plain_app_tuple;
    tmp_level_name_5 = const_int_0;
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 1;
    tmp_import_name_from_1 = IMPORT_MODULE5( tmp_name_name_5, tmp_globals_name_5, tmp_locals_name_5, tmp_fromlist_name_5, tmp_level_name_5 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_app );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_app, tmp_assign_source_8 );
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_app );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_app );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyUnicode_FromFormat( "name '%s' is not defined", "app" );
        exception_tb = NULL;
        NORMALIZE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
        CHAIN_EXCEPTION( exception_value );

        exception_lineno = 3;

        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_run );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto frame_exception_exit_1;
    }
    tmp_kw_name_1 = PyDict_Copy( const_dict_7fb9f6337f7279e2616a973f96b3d41f );
    frame_1b652b4e81dbb43643af3b231195f18b->m_frame.f_lineno = 3;
    tmp_unused = CALL_FUNCTION_WITH_KEYARGS( tmp_called_name_1, tmp_kw_name_1 );
    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_kw_name_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_1b652b4e81dbb43643af3b231195f18b );
#endif
    popFrameStack();

    assertFrameObject( frame_1b652b4e81dbb43643af3b231195f18b );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_1b652b4e81dbb43643af3b231195f18b );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_1b652b4e81dbb43643af3b231195f18b, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_1b652b4e81dbb43643af3b231195f18b->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_1b652b4e81dbb43643af3b231195f18b, exception_lineno );
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    return MOD_RETURN_VALUE( module___main__ );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
