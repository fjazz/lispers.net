# -----------------------------------------------------------------------------
#             
# Copyright 2013-2019 lispers.net - Dino Farinacci <farinacci@gmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.    
# 
# -----------------------------------------------------------------------------
#
# lisp-rtr.py
#
# This file performs LISP Reencapsualting Tunnel Router (RTR) functionality.
#
# -----------------------------------------------------------------------------
if 64 - 64: i11iIiiIii
import lisp
import lispconfig
import socket
import time
import select
import threading
import pcappy
import os
import copy
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
II1iII1i = [ None , None , None ]
oO0oIIII = None
Oo0oO0oo0oO00 = None
i111I = None
II1Ii1iI1i = lisp . lisp_get_ephemeral_port ( )
iiI1iIiI = None
OOo = None
Ii1IIii11 = None
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
OOo000 = [ ]
if 82 - 82: I11i . I1Ii111 / IiII % II111iiii % iIii1I11I1II1 % IiII
if 86 - 86: OoOoOO00 % I1IiiI
if 80 - 80: OoooooooOO . I1IiiI
if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
if 58 - 58: i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
if 31 - 31: OoO0O00 + II111iiii
def i11IiIiiIIIII ( parameter ) :
 global OOo000
 if 22 - 22: Ii1I * O0 / o0oOOo0O0Ooo
 return ( lispconfig . lisp_itr_rtr_show_command ( parameter , "RTR" ,
 OOo000 ) )
 if 64 - 64: Ii1I % i1IIi % OoooooooOO
 if 3 - 3: iII111i + O0
 if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
 if 78 - 78: OoO0O00
 if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
 if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
def i1iIIIiI1I ( parameter ) :
 global OOo000
 if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
 return ( lispconfig . lisp_itr_rtr_show_command ( parameter , "RTR" , OOo000 ,
 True ) )
 if 23 - 23: i11iIiiIii + I1IiiI
 if 68 - 68: OoOoOO00 . oO0o . i11iIiiIii
 if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
 if 33 - 33: Ii1I + II111iiii % i11iIiiIii . ooOoO0o - I1IiiI
 if 66 - 66: Ii1I - OoooooooOO * OoooooooOO . OOooOOo . I1ii11iIi11i
 if 22 - 22: OoooooooOO % I11i - iII111i . iIii1I11I1II1 * i11iIiiIii
 if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . IiII
def o0OOOOO00o0O0 ( parameter ) :
 return ( lispconfig . lisp_show_crypto_list ( "RTR" ) )
 if 71 - 71: ooOoO0o % iII111i / o0oOOo0O0Ooo
 if 49 - 49: II111iiii % iII111i * O0
 if 89 - 89: oO0o + Oo0Ooo
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
 if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
 if 20 - 20: o0oOOo0O0Ooo
def oO00 ( kv_pair ) :
 lispconfig . lisp_database_mapping_command ( kv_pair )
 if 53 - 53: OoooooooOO . i1IIi
 if 18 - 18: o0oOOo0O0Ooo
 if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
 if 95 - 95: OoO0O00 % oO0o . O0
 if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
 if 53 - 53: IiII + I1IiiI * oO0o
 if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
def o00O ( parameter ) :
 return ( lispconfig . lisp_itr_rtr_show_rloc_probe_command ( "RTR" ) )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 if 4 - 4: II111iiii / ooOoO0o . iII111i
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 if 50 - 50: I1IiiI
 if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
 if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
def II1i1IiiIIi11 ( mc , parms ) :
 iI1Ii11iII1 , Oo0O0O0ooO0O , IIIIii , O0o0 = parms
 if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
 oO0OOoO0 = "{}:{}" . format ( Oo0O0O0ooO0O . print_address_no_iid ( ) , IIIIii )
 I111Ii111 = lisp . green ( mc . print_eid_tuple ( ) , False )
 i111IiI1I = "Changed '{}' translated address:port to {} for EID {}, {} {}" . format ( O0o0 , lisp . red ( oO0OOoO0 , False ) , I111Ii111 , "{}" , "{}" )
 if 70 - 70: Ii1I . Oo0Ooo / o0oOOo0O0Ooo . Ii1I - O0 / IiII
 if 62 - 62: iIii1I11I1II1 * OoOoOO00
 for i1 in mc . rloc_set :
  if ( i1 . rle ) :
   for OOO in i1 . rle . rle_nodes :
    if ( OOO . rloc_name != O0o0 ) : continue
    OOO . store_translated_rloc ( Oo0O0O0ooO0O , IIIIii )
    Oo0oOOo = OOO . address . print_address_no_iid ( ) + ":" + str ( OOO . translated_port )
    if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
    lisp . lprint ( i111IiI1I . format ( "RLE" , Oo0oOOo ) )
    if 75 - 75: oO0o
    if 50 - 50: Ii1I / Oo0Ooo - oO0o - I11i % iII111i - oO0o
    if 91 - 91: OoO0O00 / I11i - II111iiii . I11i
  if ( i1 . rloc_name != O0o0 ) : continue
  if 18 - 18: o0oOOo0O0Ooo
  if 98 - 98: iII111i * iII111i / iII111i + I11i
  if 34 - 34: ooOoO0o
  if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
  if 92 - 92: iII111i . I1Ii111
  Oo0oOOo = i1 . rloc . print_address_no_iid ( ) + ":" + str ( i1 . translated_port )
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  if ( lisp . lisp_crypto_keys_by_rloc_encap . has_key ( Oo0oOOo ) ) :
   o000O0o = lisp . lisp_crypto_keys_by_rloc_encap [ Oo0oOOo ]
   lisp . lisp_crypto_keys_by_rloc_encap [ oO0OOoO0 ] = o000O0o
   if 42 - 42: OoOoOO00
   if 41 - 41: Oo0Ooo . ooOoO0o + O0 * o0oOOo0O0Ooo % Oo0Ooo * Oo0Ooo
   if 19 - 19: iII111i
   if 46 - 46: I1ii11iIi11i - Ii1I . iIii1I11I1II1 / I1ii11iIi11i
   if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
  i1 . delete_from_rloc_probe_list ( mc . eid , mc . group )
  i1 . store_translated_rloc ( Oo0O0O0ooO0O , IIIIii )
  i1 . add_to_rloc_probe_list ( mc . eid , mc . group )
  lisp . lprint ( i111IiI1I . format ( "RLOC" , Oo0oOOo ) )
  if 13 - 13: OOooOOo / i11iIiiIii
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  if 52 - 52: o0oOOo0O0Ooo
  if 95 - 95: Ii1I
  if ( lisp . lisp_rloc_probing ) :
   O0oOO0O = None if ( mc . group . is_null ( ) ) else mc . eid
   oO = mc . eid if ( mc . group . is_null ( ) ) else mc . group
   lisp . lisp_send_map_request ( iI1Ii11iII1 , 0 , O0oOO0O , oO , i1 )
   if 7 - 7: o0oOOo0O0Ooo - I1IiiI
   if 100 - 100: oO0o + I11i . OOooOOo * Ii1I
   if 73 - 73: i1IIi + I1IiiI
   if 46 - 46: OoO0O00 . Oo0Ooo - OoooooooOO
   if 93 - 93: iII111i
   if 10 - 10: I11i
 lisp . lisp_write_ipc_map_cache ( True , mc )
 return ( True , parms )
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
 if 57 - 57: oO0o . I11i . i1IIi
 if 42 - 42: I11i + I1ii11iIi11i % O0
def i1iIIIi1i ( mc , parms ) :
 if 43 - 43: OoOoOO00 % OOooOOo
 if 5 - 5: i11iIiiIii - i1IIi / iIii1I11I1II1
 if 26 - 26: I11i . OoooooooOO
 if 39 - 39: iII111i - O0 % i11iIiiIii * I1Ii111 . IiII
 if ( mc . group . is_null ( ) ) : return ( II1i1IiiIIi11 ( mc , parms ) )
 if 58 - 58: OoO0O00 % i11iIiiIii . iII111i / oO0o
 if ( mc . source_cache == None ) : return ( True , parms )
 if 84 - 84: iII111i . I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
 if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
 if 51 - 51: O0 + iII111i
 mc . source_cache . walk_cache ( II1i1IiiIIi11 , parms )
 return ( True , parms )
 if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
 if 48 - 48: O0
 if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
 if 41 - 41: Ii1I - O0 - O0
 if 68 - 68: OOooOOo % I1Ii111
 if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
 if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
 if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
def i1I1iI1iIi111i ( sockets , hostname , rloc , port ) :
 lisp . lisp_map_cache . walk_cache ( i1iIIIi1i ,
 [ sockets , rloc , port , hostname ] )
 return
 if 44 - 44: i1IIi % II111iiii + I11i
 if 45 - 45: iII111i / iII111i + I1Ii111 + ooOoO0o
 if 47 - 47: o0oOOo0O0Ooo + ooOoO0o
 if 82 - 82: II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
 if 77 - 77: iIii1I11I1II1 * OoO0O00
 if 95 - 95: I1IiiI + i11iIiiIii
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if 80 - 80: II111iiii
def O0O ( lisp_packet , thread_name ) :
 global II1iII1i , i1I1I , iiI1I
 global iiI1iIiI , OOo
 if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - OOooOOo + O0
 oO0OOOO0 = lisp_packet
 if 26 - 26: Ii1I
 if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
 if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 oO0 = oO0OOOO0 . packet
 O0OO0O = oO0
 O0OO0O , OO , IIIIii , OoOoO = lisp . lisp_is_rloc_probe ( O0OO0O , - 1 )
 if ( oO0 != O0OO0O ) :
  if ( OO == None ) : return
  lisp . lisp_parse_packet ( II1iII1i , O0OO0O , OO , IIIIii , OoOoO )
  return
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
  if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 oO0OOOO0 . packet = lisp . lisp_reassemble ( oO0OOOO0 . packet )
 if ( oO0OOOO0 . packet == None ) : return
 if 57 - 57: OoO0O00 / ooOoO0o
 if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
 if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
 if 13 - 13: Ii1I . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 if ( lisp . lisp_flow_logging ) : oO0OOOO0 = copy . deepcopy ( oO0OOOO0 )
 if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
 if ( oO0OOOO0 . decode ( True , None , lisp . lisp_decap_stats ) == None ) : return
 if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
 if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 oO0OOOO0 . print_packet ( "Receive-({})" . format ( thread_name ) , True )
 if 63 - 63: OoOoOO00 * iII111i
 if 69 - 69: O0 . OoO0O00
 if 49 - 49: I1IiiI - I11i
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 oO0OOOO0 . strip_outer_headers ( )
 if 62 - 62: OoooooooOO * I1IiiI
 if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
 if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
 if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
 if 77 - 77: OOooOOo * iIii1I11I1II1
 if 98 - 98: I1IiiI % Ii1I * OoooooooOO
 if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
 if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
 if 71 - 71: Oo0Ooo % OOooOOo
 if ( oO0OOOO0 . lisp_header . get_instance_id ( ) == 0xffffff ) :
  O00oO000O0O = lisp . lisp_control_header ( )
  O00oO000O0O . decode ( oO0OOOO0 . packet )
  if ( O00oO000O0O . is_info_request ( ) ) :
   I1i1i1iii = lisp . lisp_info ( )
   I1i1i1iii . decode ( oO0OOOO0 . packet )
   I1i1i1iii . print_info ( )
   if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
   if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
   if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
   if 71 - 71: I1Ii111 + Ii1I
   if 28 - 28: OOooOOo
   I11ii1IIiIi = I1i1i1iii . hostname if ( I1i1i1iii . hostname != None ) else ""
   OoOOo0OOoO = oO0OOOO0 . outer_source
   ooO0O00Oo0o = oO0OOOO0 . udp_sport
   if ( lisp . lisp_store_nat_info ( I11ii1IIiIi , OoOOo0OOoO , ooO0O00Oo0o ) ) :
    i1I1iI1iIi111i ( II1iII1i , I11ii1IIiIi , OoOOo0OOoO , ooO0O00Oo0o )
    if 65 - 65: I1ii11iIi11i . I11i - I1Ii111 * IiII / I1Ii111 / ooOoO0o
  else :
   OO = oO0OOOO0 . outer_source . print_address_no_iid ( )
   OoOoO = oO0OOOO0 . outer_ttl
   oO0OOOO0 = oO0OOOO0 . packet
   if ( lisp . lisp_is_rloc_probe_request ( oO0OOOO0 [ 28 ] ) == False and
 lisp . lisp_is_rloc_probe_reply ( oO0OOOO0 [ 28 ] ) == False ) : OoOoO = - 1
   oO0OOOO0 = oO0OOOO0 [ 28 : : ]
   lisp . lisp_parse_packet ( II1iII1i , oO0OOOO0 , OO , 0 , OoOoO )
   if 40 - 40: ooOoO0o * IiII * i11iIiiIii
  return
  if 57 - 57: ooOoO0o
  if 29 - 29: OoOoOO00 - IiII * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
  if 74 - 74: Ii1I - IiII / iII111i * O0 - OOooOOo
  if 19 - 19: I1IiiI
  if 25 - 25: Ii1I / ooOoO0o
  if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
 if ( lisp . lisp_ipc_data_plane ) :
  lisp . dprint ( "Drop packet, external data-plane active" )
  return
  if 71 - 71: I1Ii111 . II111iiii
  if 62 - 62: OoooooooOO . I11i
  if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
  if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if 58 - 58: I1IiiI
 lisp . lisp_decap_stats [ "good-packets" ] . increment ( len ( oO0OOOO0 . packet ) )
 if 53 - 53: i1IIi
 if 59 - 59: o0oOOo0O0Ooo
 if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
 if 73 - 73: I11i % i11iIiiIii - I1IiiI
 if ( oO0OOOO0 . inner_dest . is_mac ( ) ) :
  oO0OOOO0 . packet = lisp . lisp_mac_input ( oO0OOOO0 . packet )
  if ( oO0OOOO0 . packet == None ) : return
  oO0OOOO0 . encap_port = lisp . LISP_VXLAN_DATA_PORT
 elif ( oO0OOOO0 . inner_version == 4 ) :
  oO0OOOO0 . packet = lisp . lisp_ipv4_input ( oO0OOOO0 . packet )
  if ( oO0OOOO0 . packet == None ) : return
  oO0OOOO0 . inner_ttl = oO0OOOO0 . outer_ttl
 elif ( oO0OOOO0 . inner_version == 6 ) :
  oO0OOOO0 . packet = lisp . lisp_ipv6_input ( oO0OOOO0 )
  if ( oO0OOOO0 . packet == None ) : return
  oO0OOOO0 . inner_ttl = oO0OOOO0 . outer_ttl
 else :
  lisp . dprint ( "Cannot parse inner packet header" )
  return
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
 Ii1Iii1iIi = lisp . lisp_map_cache_lookup ( oO0OOOO0 . inner_source , oO0OOOO0 . inner_dest )
 if 82 - 82: I1ii11iIi11i / I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
 if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
 if 15 - 15: OoOoOO00 % I1IiiI * I11i
 if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
 if 20 - 20: oO0o % IiII
 if ( Ii1Iii1iIi and ( Ii1Iii1iIi . action == lisp . LISP_NATIVE_FORWARD_ACTION or
 Ii1Iii1iIi . eid . address == 0 ) ) :
  III1i1i11i = lisp . lisp_db_for_lookups . lookup_cache ( oO0OOOO0 . inner_source , False )
  if ( III1i1i11i and III1i1i11i . secondary_iid ) :
   oOo0 = oO0OOOO0 . inner_dest
   oOo0 . instance_id = III1i1i11i . secondary_iid
   Ii1Iii1iIi = lisp . lisp_map_cache_lookup ( oO0OOOO0 . inner_source , oOo0 )
   if 56 - 56: o0oOOo0O0Ooo + II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
   if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
   if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
 if ( Ii1Iii1iIi == None or Ii1Iii1iIi . action == lisp . LISP_SEND_MAP_REQUEST_ACTION ) :
  if ( lisp . lisp_rate_limit_map_request ( oO0OOOO0 . inner_source ,
 oO0OOOO0 . inner_dest ) ) : return
  lisp . lisp_send_map_request ( II1iII1i , II1Ii1iI1i ,
 oO0OOOO0 . inner_source , oO0OOOO0 . inner_dest , None )
  return
  if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
  if 48 - 48: O0
  if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
 if ( Ii1Iii1iIi and Ii1Iii1iIi . is_active ( ) and Ii1Iii1iIi . has_ttl_elapsed ( ) ) :
  lisp . lprint ( "Refresh map-cache entry {}" . format ( lisp . green ( Ii1Iii1iIi . print_eid_tuple ( ) , False ) ) )
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
  lisp . lisp_send_map_request ( II1iII1i , II1Ii1iI1i ,
 oO0OOOO0 . inner_source , oO0OOOO0 . inner_dest , None )
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
  if 60 - 60: II111iiii + Oo0Ooo
  if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
 Ii1Iii1iIi . stats . increment ( len ( oO0OOOO0 . packet ) )
 if 49 - 49: II111iiii
 if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
 if 81 - 81: iII111i + IiII
 if 98 - 98: I1IiiI
 o00o0 , II1I , II1I1I1Ii , OOOOoO00o0O , I1I1I1IIi1III = Ii1Iii1iIi . select_rloc ( oO0OOOO0 , None )
 if 5 - 5: Oo0Ooo % ooOoO0o % i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - I1ii11iIi11i
 if ( o00o0 == None and I1I1I1IIi1III == None ) :
  if ( OOOOoO00o0O == lisp . LISP_NATIVE_FORWARD_ACTION ) :
   lisp . dprint ( "Natively forwarding" )
   oO0OOOO0 . send_packet ( iiI1iIiI , oO0OOOO0 . inner_dest )
   return
   if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
  lisp . dprint ( "No reachable RLOCs found" )
  return
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
 if ( o00o0 and o00o0 . is_null ( ) ) :
  lisp . dprint ( "Drop action RLOC found" )
  return
  if 46 - 46: OoOoOO00 + OoO0O00
  if 70 - 70: iII111i / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
  if 96 - 96: OoooooooOO + oO0o
  if 44 - 44: oO0o
 oO0OOOO0 . outer_tos = oO0OOOO0 . inner_tos
 oO0OOOO0 . outer_ttl = oO0OOOO0 . inner_ttl
 if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
 if 88 - 88: OoOoOO00 / II111iiii
 if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
 if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
 if ( o00o0 ) :
  oO0OOOO0 . encap_port = II1I
  if ( II1I == 0 ) : oO0OOOO0 . encap_port = lisp . LISP_DATA_PORT
  oO0OOOO0 . outer_dest . copy_address ( o00o0 )
  iiI1I1 = oO0OOOO0 . outer_dest . afi_to_version ( )
  oO0OOOO0 . outer_version = iiI1I1
  ooO = lisp . lisp_myrlocs [ 0 ] if ( iiI1I1 == 4 ) else lisp . lisp_myrlocs [ 1 ]
  if 6 - 6: iIii1I11I1II1 . ooOoO0o % o0oOOo0O0Ooo
  oO0OOOO0 . outer_source . copy_address ( ooO )
  if 50 - 50: iII111i + O0 + Ii1I . II111iiii / o0oOOo0O0Ooo
  if 17 - 17: Ii1I % iIii1I11I1II1 - iIii1I11I1II1
  if 78 - 78: iII111i + I11i . ooOoO0o - iII111i . Ii1I
  if 30 - 30: I1IiiI + OoO0O00 % Ii1I * iII111i / Oo0Ooo - I11i
  if ( oO0OOOO0 . encode ( II1I1I1Ii ) == None ) : return
  if ( len ( oO0OOOO0 . packet ) <= 1500 ) : oO0OOOO0 . print_packet ( "Send" , True )
  if 64 - 64: iIii1I11I1II1
  if 21 - 21: Oo0Ooo . II111iiii
  if 54 - 54: II111iiii % II111iiii
  if 86 - 86: O0 % Ii1I * ooOoO0o * iIii1I11I1II1 * i1IIi * I11i
  OOOoOOO0oO = OOo if iiI1I1 == 6 else iiI1iIiI
  oO0OOOO0 . send_packet ( OOOoOOO0oO , oO0OOOO0 . outer_dest )
  if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
 elif ( I1I1I1IIi1III ) :
  if 54 - 54: i1IIi + II111iiii
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if 5 - 5: Ii1I
  if 46 - 46: IiII
  ii1iIi1iIiI1i = len ( oO0OOOO0 . packet )
  for iiI1iIii1i in I1I1I1IIi1III . rle_forwarding_list :
   oO0OOOO0 . outer_dest . copy_address ( iiI1iIii1i . address )
   oO0OOOO0 . encap_port = lisp . LISP_DATA_PORT if iiI1iIii1i . translated_port == 0 else iiI1iIii1i . translated_port
   if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . IiII
   if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
   iiI1I1 = oO0OOOO0 . outer_dest . afi_to_version ( )
   oO0OOOO0 . outer_version = iiI1I1
   ooO = lisp . lisp_myrlocs [ 0 ] if ( iiI1I1 == 4 ) else lisp . lisp_myrlocs [ 1 ]
   if 63 - 63: OoO0O00
   oO0OOOO0 . outer_source . copy_address ( ooO )
   if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
   if ( oO0OOOO0 . encode ( None ) == None ) : return
   if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   oO0OOOO0 . print_packet ( "Replicate-to-L{}" . format ( iiI1iIii1i . level ) , True )
   oO0OOOO0 . send_packet ( iiI1iIiI , oO0OOOO0 . outer_dest )
   if 75 - 75: IiII . ooOoO0o
   if 50 - 50: OoOoOO00
   if 60 - 60: ooOoO0o * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
   if 69 - 69: Ii1I * O0 . i11iIiiIii / Ii1I . o0oOOo0O0Ooo
   if 63 - 63: I11i + o0oOOo0O0Ooo . II111iiii - I1IiiI
   oOOO00o000o = len ( oO0OOOO0 . packet ) - ii1iIi1iIiI1i
   oO0OOOO0 . packet = oO0OOOO0 . packet [ oOOO00o000o : : ]
   if 9 - 9: oO0o + I11i / I11i
   if ( lisp . lisp_flow_logging ) : oO0OOOO0 = copy . deepcopy ( oO0OOOO0 )
   if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
   if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
   if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
   if 51 - 51: IiII
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
   if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
 del ( oO0OOOO0 )
 return
 if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
 if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 if 97 - 97: I1IiiI / iII111i
 if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
def Iiiiii111i1ii ( lisp_thread ) :
 lisp . lisp_set_exception ( )
 while ( True ) :
  if 25 - 25: OOooOOo - ooOoO0o / i11iIiiIii
  if 41 - 41: i1IIi % iII111i + iIii1I11I1II1
  if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
  if 3 - 3: I1Ii111
  oO0OOOO0 = lisp_thread . input_queue . get ( )
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  lisp_thread . input_stats . increment ( len ( oO0OOOO0 ) )
  if 7 - 7: OoooooooOO . IiII
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  lisp_thread . lisp_packet . packet = oO0OOOO0
  if 92 - 92: ooOoO0o
  if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
  if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  O0O ( lisp_thread . lisp_packet , lisp_thread . thread_name )
  if 92 - 92: I11i . I1Ii111
 return
 if 85 - 85: I1ii11iIi11i . I1Ii111
 if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
 if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
 if 18 - 18: iIii1I11I1II1 % I11i
 if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
 if 75 - 75: OoooooooOO * IiII
 if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
def o0 ( thread ) :
 iiiI1I1iIIIi1 = ( time . time ( ) % thread . number_of_pcap_threads )
 return ( int ( iiiI1I1iIIIi1 ) == thread . thread_number )
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
 if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
 if 85 - 85: OoOoOO00 + OOooOOo
 if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
 if 27 - 27: Ii1I
 if 67 - 67: I1IiiI
 if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
 if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
def OO0 ( parms , not_used , packet ) :
 if ( o0 ( parms [ 1 ] ) == False ) : return
 if 44 - 44: iII111i - I1Ii111 / O0 * Oo0Ooo + II111iiii / OoOoOO00
 OOOOoO000 = parms [ 0 ]
 oOOOO = parms [ 1 ]
 Ii = oOOOO . number_of_worker_threads
 if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
 oOOOO . input_stats . increment ( len ( packet ) )
 if 90 - 90: iII111i
 if 31 - 31: OOooOOo + O0
 if 87 - 87: ooOoO0o
 if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
 if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
 if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 iIi1II = 4 if OOOOoO000 == "lo0" else ( 14 if lisp . lisp_is_macos ( ) else 16 )
 packet = packet [ iIi1II : : ]
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
 if 77 - 77: I1Ii111
 if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
 if ( Ii ) :
  iI11I = oOOOO . input_stats . packet_count % Ii
  iI11I = iI11I + ( len ( OOo000 ) - Ii )
  I1IIIiii1 = OOo000 [ iI11I ]
  I1IIIiii1 . input_queue . put ( packet )
 else :
  oOOOO . lisp_packet . packet = packet
  O0O ( oOOOO . lisp_packet , oOOOO . thread_name )
  if 65 - 65: I11i / II111iiii * Ii1I . iII111i * oO0o % OOooOOo
 return
 if 69 - 69: ooOoO0o - OoO0O00 / i11iIiiIii + I1ii11iIi11i % OoooooooOO
 if 73 - 73: Ii1I - I1Ii111
 if 68 - 68: iII111i * OoooooooOO * iIii1I11I1II1 . II111iiii
 if 81 - 81: OOooOOo / O0 + I11i + Ii1I / I1IiiI
 if 27 - 27: OoOoOO00 * IiII
 if 59 - 59: IiII . IiII - II111iiii + IiII . i1IIi . OoO0O00
 if 57 - 57: I1IiiI + Ii1I % oO0o + oO0o / II111iiii . Ii1I
def I1iIII1 ( lisp_thread ) :
 lisp . lisp_set_exception ( )
 if ( lisp . lisp_myrlocs [ 0 ] == None ) : return
 if 39 - 39: OoooooooOO
 OOOOoO000 = "lo0" if lisp . lisp_is_macos ( ) else "any"
 if 38 - 38: I1IiiI
 oOo0OoOOo0 = pcappy . open_live ( OOOOoO000 , 9000 , 0 , 100 )
 if 30 - 30: I1ii11iIi11i % I1IiiI
 O0Oo00 = "(dst host "
 ii1IiIIi1i = ""
 for oO0OOoO0 in lisp . lisp_get_all_addresses ( ) :
  O0Oo00 += "{} or " . format ( oO0OOoO0 )
  ii1IiIIi1i += "{} or " . format ( oO0OOoO0 )
  if 54 - 54: ooOoO0o
 O0Oo00 = O0Oo00 [ 0 : - 4 ]
 O0Oo00 += ") and ((udp dst port 4341 or 8472 or 4789) or "
 O0Oo00 += "(proto 17 and (ip[6]&0xe0 == 0x20 or " + "(ip[6]&0xe0 == 0 and ip[7] != 0))))"
 if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
 if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
 if 30 - 30: OoOoOO00
 if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
 if 26 - 26: II111iiii * OoOoOO00
 ii1IiIIi1i = ii1IiIIi1i [ 0 : - 4 ]
 O0Oo00 += ( " or (not (src host {}) and " + "((udp src port 4342 and ip[28] == 0x28) or " + "(udp dst port 4342 and ip[28] == 0x12)))" ) . format ( ii1IiIIi1i )
 if 10 - 10: II111iiii . iII111i
 if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
 if 88 - 88: iII111i
 lisp . lprint ( "Capturing packets for: '{}'" . format ( O0Oo00 ) )
 oOo0OoOOo0 . filter = O0Oo00
 if 19 - 19: II111iiii * IiII + Ii1I
 if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
 if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
 if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
 oOo0OoOOo0 . loop ( - 1 , OO0 , [ OOOOoO000 , lisp_thread ] )
 return
 if 67 - 67: I11i - OOooOOo . i1IIi
 if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
 if 87 - 87: OoOoOO00
 if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
 if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
 if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
 if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
def OO0oo ( ) :
 lisp . lisp_set_exception ( )
 if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
 if 11 - 11: iII111i * Ii1I - OoOoOO00
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
 if 74 - 74: Oo0Ooo
 for o000O0o in lisp . lisp_crypto_keys_by_nonce . values ( ) :
  for OO000o00 in o000O0o : del ( OO000o00 )
  if 46 - 46: OoO0O00
 lisp . lisp_crypto_keys_by_nonce = { }
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
 if 68 - 68: OoooooooOO % II111iiii
 lisp . lisp_timeout_map_cache ( lisp . lisp_map_cache )
 if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
 if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
 if 2 - 2: Ii1I - IiII
 if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
 Ii1IIii11 = threading . Timer ( 60 , OO0oo , [ ] )
 Ii1IIii11 . start ( )
 return
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
 if 71 - 71: OoooooooOO
 if 33 - 33: I1Ii111
 if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
 if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
 if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
 if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
def iiI1i1Iii111 ( ) :
 global oO0oIIII , II1iII1i , i111I
 global iiI1iIiI , OOo , OOo000
 global Oo0oO0oo0oO00
 if 43 - 43: o0oOOo0O0Ooo
 lisp . lisp_i_am ( "rtr" )
 lisp . lisp_set_exception ( )
 lisp . lisp_print_banner ( "RTR starting up" )
 if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
 if 58 - 58: Oo0Ooo / oO0o
 if 44 - 44: OOooOOo
 if 54 - 54: Ii1I - I11i - I1Ii111 . iIii1I11I1II1
 if ( lisp . lisp_get_local_addresses ( ) == False ) : return ( False )
 if 79 - 79: Ii1I . OoO0O00
 if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % ooOoO0o
 if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
 if 60 - 60: I1IiiI * I1Ii111 % OoO0O00 + oO0o
 if 52 - 52: i1IIi
 if 84 - 84: Ii1I / IiII
 OOOooo0OooOoO = "0.0.0.0" if lisp . lisp_is_raspbian ( ) else "0::0"
 i111I = lisp . lisp_open_listen_socket ( OOOooo0OooOoO ,
 str ( II1Ii1iI1i ) )
 oO0oIIII = lisp . lisp_open_listen_socket ( "" , "lisp-rtr" )
 Oo0oO0oo0oO00 = lisp . lisp_open_listen_socket ( "" , "lispers.net-itr" )
 if 91 - 91: oO0o + I1IiiI
 II1iII1i [ 0 ] = i111I
 if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / I11i
 II1iII1i [ 1 ] = lisp . lisp_open_send_socket ( "" , lisp . LISP_AFI_IPV6 )
 II1iII1i [ 2 ] = oO0oIIII
 if 44 - 44: I11i . OoOoOO00 * I1IiiI + OoooooooOO - iII111i - IiII
 if 15 - 15: IiII / O0 . o0oOOo0O0Ooo . i11iIiiIii
 if 59 - 59: I1Ii111 - o0oOOo0O0Ooo - ooOoO0o
 if 48 - 48: i1IIi + I11i % OoOoOO00 / Oo0Ooo - o0oOOo0O0Ooo
 if 67 - 67: oO0o % o0oOOo0O0Ooo . OoooooooOO + OOooOOo * I11i * OoOoOO00
 if 36 - 36: O0 + Oo0Ooo
 if 5 - 5: Oo0Ooo * OoOoOO00
 if 46 - 46: ooOoO0o
 if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
 iiI1iIiI = socket . socket ( socket . AF_INET , socket . SOCK_RAW ,
 socket . IPPROTO_RAW )
 iiI1iIiI . setsockopt ( socket . SOL_IP , socket . IP_HDRINCL , 1 )
 II1iII1i . append ( iiI1iIiI )
 if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
 if ( lisp . lisp_is_raspbian ( ) == False ) :
  OOo = socket . socket ( socket . AF_INET6 , socket . SOCK_RAW ,
 socket . IPPROTO_UDP )
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  if 72 - 72: i1IIi
 OOoo0oo = os . getenv ( "LISP_PCAP_THREADS" )
 OOoo0oo = 1 if ( OOoo0oo == None ) else int ( OOoo0oo )
 ooOooo0OO = os . getenv ( "LISP_WORKER_THREADS" )
 ooOooo0OO = 0 if ( ooOooo0OO == None ) else int ( ooOooo0OO )
 if 2 - 2: II111iiii - OoO0O00 . IiII * iII111i / oO0o
 if 80 - 80: OOooOOo / I11i / OoOoOO00 + i1IIi - Oo0Ooo
 if 11 - 11: o0oOOo0O0Ooo * OoO0O00
 if 15 - 15: OoOoOO00
 for oOoOoO000OO in range ( OOoo0oo ) :
  ii11II11 = lisp . lisp_thread ( "pcap-{}" . format ( oOoOoO000OO ) )
  ii11II11 . thread_number = oOoOoO000OO
  ii11II11 . number_of_pcap_threads = OOoo0oo
  ii11II11 . number_of_worker_threads = ooOooo0OO
  OOo000 . append ( ii11II11 )
  threading . Thread ( target = I1iIII1 , args = [ ii11II11 ] ) . start ( )
  if 70 - 70: iIii1I11I1II1
  if 48 - 48: II111iiii * IiII
  if 41 - 41: Ii1I % I1ii11iIi11i
  if 12 - 12: OOooOOo
  if 69 - 69: OoooooooOO + OOooOOo
  if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
 for oOoOoO000OO in range ( ooOooo0OO ) :
  ii11II11 = lisp . lisp_thread ( "worker-{}" . format ( oOoOoO000OO ) )
  OOo000 . append ( ii11II11 )
  threading . Thread ( target = Iiiiii111i1ii , args = [ ii11II11 ] ) . start ( )
  if 31 - 31: I11i % OOooOOo * I11i
  if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
  if 1 - 1: iIii1I11I1II1
  if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
  if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
 lisp . lisp_load_checkpoint ( )
 if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
 if 4 - 4: OoooooooOO . ooOoO0o
 if 78 - 78: I1ii11iIi11i + I11i - O0
 if 10 - 10: I1Ii111 % I1IiiI
 lisp . lisp_load_split_pings = ( os . getenv ( "LISP_LOAD_SPLIT_PINGS" ) != None )
 if 97 - 97: OoooooooOO - I1Ii111
 if 58 - 58: iIii1I11I1II1 + O0
 if 30 - 30: ooOoO0o % iII111i * OOooOOo - I1ii11iIi11i * Ii1I % ooOoO0o
 if 46 - 46: i11iIiiIii - O0 . oO0o
 Ii1IIii11 = threading . Timer ( 60 , OO0oo , [ ] )
 Ii1IIii11 . start ( )
 return ( True )
 if 100 - 100: I1IiiI / o0oOOo0O0Ooo * iII111i . O0 / OOooOOo
 if 83 - 83: I1Ii111
 if 48 - 48: II111iiii * OOooOOo * I1Ii111
 if 50 - 50: IiII % i1IIi
 if 21 - 21: OoooooooOO - iIii1I11I1II1
 if 93 - 93: oO0o - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - ooOoO0o
 if 90 - 90: ooOoO0o + II111iiii * I1ii11iIi11i / Ii1I . o0oOOo0O0Ooo + o0oOOo0O0Ooo
def I11I ( ) :
 if 69 - 69: i1IIi
 if 59 - 59: II111iiii - o0oOOo0O0Ooo
 if 24 - 24: Oo0Ooo - i1IIi + I11i
 if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
 lisp . lisp_close_socket ( II1iII1i [ 0 ] , "" )
 lisp . lisp_close_socket ( II1iII1i [ 1 ] , "" )
 lisp . lisp_close_socket ( oO0oIIII , "lisp-rtr" )
 lisp . lisp_close_socket ( i111I , "" )
 lisp . lisp_close_socket ( Oo0oO0oo0oO00 , "lispers.net-itr" )
 iiI1iIiI . close ( )
 return
 if 96 - 96: iII111i
 if 18 - 18: iII111i * I11i - Ii1I
 if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oO0o
 if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
 if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
def iiIiI ( kv_pair ) :
 global II1iII1i
 global II1Ii1iI1i
 if 87 - 87: ooOoO0o - OoooooooOO + i11iIiiIii
 lispconfig . lisp_map_resolver_command ( kv_pair )
 if 73 - 73: I11i * OoooooooOO . O0 . IiII
 if ( lisp . lisp_test_mr_timer == None or
 lisp . lisp_test_mr_timer . is_alive ( ) == False ) :
  lisp . lisp_test_mr_timer = threading . Timer ( 2 , lisp . lisp_test_mr ,
 [ II1iII1i , II1Ii1iI1i ] )
  lisp . lisp_test_mr_timer . start ( )
  if 55 - 55: Oo0Ooo
 return
 if 77 - 77: II111iiii
 if 16 - 16: I1IiiI * II111iiii / iIii1I11I1II1 - iII111i
 if 3 - 3: I1IiiI * ooOoO0o + II111iiii - OoO0O00
 if 97 - 97: I1ii11iIi11i / oO0o - o0oOOo0O0Ooo - I1IiiI - I1IiiI
 if 54 - 54: Oo0Ooo + I1IiiI / iII111i . I1IiiI * OoOoOO00
 if 1 - 1: OoOoOO00 * OoO0O00 . i1IIi / Oo0Ooo . I1ii11iIi11i + Oo0Ooo
 if 17 - 17: Oo0Ooo + OoO0O00 / Ii1I / iII111i * OOooOOo
 if 29 - 29: OoO0O00 % OoooooooOO * oO0o / II111iiii - oO0o
def iI ( kv_pair ) :
 global i111I , iiI1iIiI , II1Ii1iI1i
 if 19 - 19: II111iiii
 OoOO = lisp . lisp_rloc_probing
 if 32 - 32: OoOoOO00 * I1IiiI % ooOoO0o * Ii1I . O0
 if 48 - 48: iII111i * iII111i
 if 13 - 13: Ii1I / I11i + OoOoOO00 . o0oOOo0O0Ooo % ooOoO0o
 if 48 - 48: I1IiiI / i11iIiiIii - o0oOOo0O0Ooo * oO0o / OoooooooOO
 lispconfig . lisp_xtr_command ( kv_pair )
 if 89 - 89: iIii1I11I1II1 / I1IiiI - II111iiii / Ii1I . i11iIiiIii . Ii1I
 if 48 - 48: O0 + O0 . I1Ii111 - ooOoO0o
 if 63 - 63: oO0o
 if 71 - 71: i1IIi . Ii1I * iII111i % OoooooooOO + OOooOOo
 if 36 - 36: IiII
 if ( OoOO == False and lisp . lisp_rloc_probing ) :
  iI1Ii11iII1 = [ i111I , i111I ,
 None , iiI1iIiI ]
  lisp . lisp_start_rloc_probe_timer ( 1 , iI1Ii11iII1 )
  i1iiI = { "type" : "itr-crypto-port" , "port" : II1Ii1iI1i }
  lisp . lisp_write_to_dp_socket ( i1iiI )
  if 74 - 74: I1Ii111 % I1ii11iIi11i
  if 7 - 7: II111iiii
  if 27 - 27: oO0o . OoooooooOO + i11iIiiIii
  if 86 - 86: I11i / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + oO0o
  if 33 - 33: o0oOOo0O0Ooo . iII111i . IiII . i1IIi
 lisp . lisp_ipc_write_xtr_parameters ( lisp . lisp_debug_logging ,
 lisp . lisp_data_plane_logging )
 return
 if 49 - 49: I1ii11iIi11i
 if 84 - 84: I11i - Oo0Ooo / O0 - I1Ii111
 if 21 - 21: O0 * O0 % I1ii11iIi11i
 if 94 - 94: I11i + II111iiii % i11iIiiIii
 if 8 - 8: ooOoO0o * O0
OOoO = {
 "lisp xtr-parameters" : [ iI , {
 "rloc-probing" : [ True , "yes" , "no" ] ,
 "nonce-echoing" : [ True , "yes" , "no" ] ,
 "data-plane-security" : [ True , "yes" , "no" ] ,
 "data-plane-logging" : [ True , "yes" , "no" ] ,
 "flow-logging" : [ True , "yes" , "no" ] ,
 "nat-traversal" : [ True , "yes" , "no" ] ,
 "checkpoint-map-cache" : [ True , "yes" , "no" ] ,
 "ipc-data-plane" : [ True , "yes" , "no" ] ,
 "program-hardware" : [ True , "yes" , "no" ] } ] ,

 "lisp map-resolver" : [ iiIiI , {
 "mr-name" : [ True ] ,
 "ms-name" : [ True ] ,
 "dns-name" : [ True ] ,
 "address" : [ True ] } ] ,

 "lisp map-cache" : [ lispconfig . lisp_map_cache_command , {
 "prefix" : [ ] ,
 "mr-name" : [ True ] ,
 "ms-name" : [ True ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "send-map-request" : [ True , "yes" , "no" ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "address" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "lisp rtr-map-cache" : [ lispconfig . lisp_map_cache_command , {
 "prefix" : [ ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "address" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "lisp explicit-locator-path" : [ lispconfig . lisp_elp_command , {
 "elp-name" : [ False ] ,
 "elp-node" : [ ] ,
 "address" : [ True ] ,
 "probe" : [ True , "yes" , "no" ] ,
 "strict" : [ True , "yes" , "no" ] ,
 "eid" : [ True , "yes" , "no" ] } ] ,

 "lisp replication-list-entry" : [ lispconfig . lisp_rle_command , {
 "rle-name" : [ False ] ,
 "rle-node" : [ ] ,
 "address" : [ True ] ,
 "level" : [ True , 0 , 255 ] } ] ,

 "lisp json" : [ lispconfig . lisp_json_command , {
 "json-name" : [ False ] ,
 "json-string" : [ False ] } ] ,

 "lisp database-mapping" : [ oO00 , {
 "prefix" : [ ] ,
 "mr-name" : [ True ] ,
 "ms-name" : [ True ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "secondary-instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "dynamic-eid" : [ True , "yes" , "no" ] ,
 "signature-eid" : [ True , "yes" , "no" ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "geo-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "json-name" : [ True ] ,
 "address" : [ True ] ,
 "interface" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "show rtr-rloc-probing" : [ o00O , { } ] ,
 "show rtr-keys" : [ o0OOOOO00o0O0 , { } ] ,
 "show rtr-map-cache" : [ i11IiIiiIIIII , { } ] ,
 "show rtr-map-cache-dns" : [ i1iIIIiI1I , { } ]
 }
if 18 - 18: iIii1I11I1II1 + Oo0Ooo - OOooOOo + OoooooooOO * OoooooooOO
if 41 - 41: ooOoO0o . Oo0Ooo + I1IiiI
if 100 - 100: Ii1I + OoO0O00
if 73 - 73: i1IIi - I1Ii111 % ooOoO0o / OoO0O00
if 40 - 40: I1ii11iIi11i * ooOoO0o - I1IiiI / IiII / i11iIiiIii
if 83 - 83: I1ii11iIi11i / I1Ii111 - i11iIiiIii . iIii1I11I1II1 + Oo0Ooo
if ( iiI1i1Iii111 ( ) == False ) :
 lisp . lprint ( "lisp_rtr_startup() failed" )
 lisp . lisp_print_banner ( "RTR abnormal exit" )
 exit ( 1 )
 if 59 - 59: O0 % Oo0Ooo
 if 92 - 92: Ii1I % iII111i / I1ii11iIi11i % I1ii11iIi11i * I1IiiI
Oo = [ i111I , oO0oIIII ,
 Oo0oO0oo0oO00 ]
oO00oOOo0Oo = [ i111I ] * 3
if 5 - 5: o0oOOo0O0Ooo . O0 / Oo0Ooo % OoO0O00
while ( True ) :
 try : OoOo , II , IiiIIIiI1ii = select . select ( Oo , [ ] , [ ] )
 except : break
 if 78 - 78: O0 * OOooOOo
 if 43 - 43: I1ii11iIi11i / I1IiiI . ooOoO0o
 if 62 - 62: iIii1I11I1II1 + iII111i . Oo0Ooo / IiII % O0 . I1Ii111
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / o0oOOo0O0Ooo / II111iiii
 if ( lisp . lisp_ipc_data_plane and Oo0oO0oo0oO00 in OoOo ) :
  lisp . lisp_process_punt ( Oo0oO0oo0oO00 , II1iII1i ,
 II1Ii1iI1i )
  if 49 - 49: OOooOOo . I1ii11iIi11i . i11iIiiIii - II111iiii / Ii1I
  if 62 - 62: OOooOOo
  if 1 - 1: IiII / IiII - i11iIiiIii
  if 87 - 87: Oo0Ooo / O0 * IiII / o0oOOo0O0Ooo
  if 19 - 19: I1Ii111 + i1IIi . I1IiiI - Oo0Ooo
 if ( i111I in OoOo ) :
  iIi1I1 , OO , IIIIii , oO0OOOO0 = lisp . lisp_receive ( oO00oOOo0Oo [ 0 ] ,
 False )
  if ( OO == "" ) : break
  if ( lisp . lisp_is_rloc_probe_request ( oO0OOOO0 [ 0 ] ) ) :
   lisp . lprint ( "RTR ignoring RLOC-probe request, using pcap" )
   continue
   if 63 - 63: iII111i * I1ii11iIi11i . OoooooooOO / OOooOOo * Oo0Ooo . ooOoO0o
  if ( lisp . lisp_is_rloc_probe_reply ( oO0OOOO0 [ 0 ] ) ) :
   lisp . lprint ( "RTR ignoring RLOC-probe reply, using pcap" )
   continue
   if 62 - 62: i1IIi / ooOoO0o . I1IiiI * o0oOOo0O0Ooo
  lisp . lisp_parse_packet ( oO00oOOo0Oo , oO0OOOO0 , OO , IIIIii )
  if 21 - 21: o0oOOo0O0Ooo
  if 81 - 81: I11i / iIii1I11I1II1 - ooOoO0o * I1Ii111 . I1IiiI * I1ii11iIi11i
  if 95 - 95: I1IiiI
  if 88 - 88: IiII % OoO0O00 + I1Ii111 + I1Ii111 * II111iiii
  if 78 - 78: OoooooooOO
  if 77 - 77: I1ii11iIi11i / i1IIi / Oo0Ooo % OOooOOo
 if ( oO0oIIII in OoOo ) :
  iIi1I1 , OO , IIIIii , oO0OOOO0 = lisp . lisp_receive ( oO0oIIII , True )
  if 48 - 48: I11i - IiII + iIii1I11I1II1 + OoooooooOO
  if ( OO == "" ) : break
  if 4 - 4: II111iiii . I11i + Ii1I * I1Ii111 . ooOoO0o
  if ( iIi1I1 == "command" ) :
   if ( oO0OOOO0 == "clear" ) :
    lisp . lisp_clear_map_cache ( )
    continue
    if 87 - 87: OoOoOO00 / OoO0O00 / i11iIiiIii
   if ( oO0OOOO0 . find ( "clear%" ) != - 1 ) :
    lispconfig . lisp_clear_decap_stats ( oO0OOOO0 )
    continue
    if 74 - 74: oO0o / I1ii11iIi11i % o0oOOo0O0Ooo
   lispconfig . lisp_process_command ( oO0oIIII , iIi1I1 ,
 oO0OOOO0 , "lisp-rtr" , [ OOoO ] )
  elif ( iIi1I1 == "api" ) :
   lisp . lisp_process_api ( "lisp-rtr" , oO0oIIII , oO0OOOO0 )
  elif ( iIi1I1 == "data-packet" ) :
   O0O ( oO0OOOO0 , "" )
  else :
   if ( lisp . lisp_is_rloc_probe_request ( oO0OOOO0 [ 0 ] ) ) :
    lisp . lprint ( "RTR ignoring RLOC-probe request, using pcap" )
    continue
    if 88 - 88: OoOoOO00 - i11iIiiIii % o0oOOo0O0Ooo * I11i + I1ii11iIi11i
   if ( lisp . lisp_is_rloc_probe_reply ( oO0OOOO0 [ 0 ] ) ) :
    lisp . lprint ( "RTR ignoring RLOC-probe reply, using pcap" )
    continue
    if 52 - 52: II111iiii . I1IiiI + OoOoOO00 % OoO0O00
   lisp . lisp_parse_packet ( II1iII1i , oO0OOOO0 , OO , IIIIii )
   if 62 - 62: o0oOOo0O0Ooo
   if 15 - 15: I11i + Ii1I . OOooOOo * OoO0O00 . OoOoOO00
   if 18 - 18: i1IIi % II111iiii + I1Ii111 % Ii1I
   if 72 - 72: iIii1I11I1II1
   if 45 - 45: Oo0Ooo - o0oOOo0O0Ooo % I1Ii111
I11I ( )
lisp . lisp_print_banner ( "RTR normal exit" )
exit ( 0 )
if 38 - 38: I1Ii111 % OOooOOo - OoooooooOO
if 87 - 87: OoO0O00 % I1IiiI
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
