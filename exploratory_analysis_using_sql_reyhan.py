# -*- coding: utf-8 -*-
"""Exploratory Analysis using SQL-reyhan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C8OLY00SLzMmduYKOwYMSnPY2FEHTMn2

# Assignment: SQL Notebook for Peer Assignment
Estimated time needed: 60 minutes.

Introduction
Using this Python notebook you will:

Understand the Spacex DataSet
Load the dataset into the corresponding table in a Db2 database
Execute SQL queries to answer assignment questions
Overview of the DataSet
SpaceX has gained worldwide attention for a series of historic milestones.

It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.

Therefore if we can determine if the first stage will land, we can determine the cost of a launch.

This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

This dataset includes a record for each payload carried during a SpaceX mission into outer space.
#REYAN

Download the datasets
This assignment requires you to load the spacex dataset.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):

![Spacex.csv](data:text/csv;base64,RGF0ZSxUaW1lIChVVEMpLEJvb3N0ZXJfVmVyc2lvbixMYXVuY2hfU2l0ZSxQYXlsb2FkLFBBWUxPQURfTUFTU19fS0dfLE9yYml0LEN1c3RvbWVyLE1pc3Npb25fT3V0Y29tZSxMYW5kaW5nX091dGNvbWUNCjIwMTAtMDYtMDQsMTg6NDU6MDAsRjkgdjEuMCAgQjAwMDMsQ0NBRlMgTEMtNDAsRHJhZ29uIFNwYWNlY3JhZnQgUXVhbGlmaWNhdGlvbiBVbml0LDAsTEVPLFNwYWNlWCxTdWNjZXNzLEZhaWx1cmUgKHBhcmFjaHV0ZSkNCjIwMTAtMTItMDgsMTU6NDM6MDAsRjkgdjEuMCAgQjAwMDQsQ0NBRlMgTEMtNDAsIkRyYWdvbiBkZW1vIGZsaWdodCBDMSwgdHdvIEN1YmVTYXRzLCBiYXJyZWwgb2YgQnJvdWVyZSBjaGVlc2UiLDAsTEVPIChJU1MpLE5BU0EgKENPVFMpIE5STyxTdWNjZXNzLEZhaWx1cmUgKHBhcmFjaHV0ZSkNCjIwMTItMDUtMjIsNzo0NDowMCxGOSB2MS4wICBCMDAwNSxDQ0FGUyBMQy00MCxEcmFnb24gZGVtbyBmbGlnaHQgQzIsNTI1LExFTyAoSVNTKSxOQVNBIChDT1RTKSxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTItMTAtMDgsMDozNTowMCxGOSB2MS4wICBCMDAwNixDQ0FGUyBMQy00MCxTcGFjZVggQ1JTLTEsNTAwLExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxMy0wMy0wMSwxNToxMDowMCxGOSB2MS4wICBCMDAwNyxDQ0FGUyBMQy00MCxTcGFjZVggQ1JTLTIsNjc3LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxMy0wOS0yOSwxNjowMDowMCxGOSB2MS4xICBCMTAwMyxWQUZCIFNMQy00RSxDQVNTSU9QRSw1MDAsUG9sYXIgTEVPLE1EQSxTdWNjZXNzLFVuY29udHJvbGxlZCAob2NlYW4pDQoyMDEzLTEyLTAzLDIyOjQxOjAwLEY5IHYxLjEsQ0NBRlMgTEMtNDAsU0VTLTgsMzE3MCxHVE8sU0VTLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxNC0wMS0wNiwyMjowNjowMCxGOSB2MS4xLENDQUZTIExDLTQwLFRoYWljb20gNiwzMzI1LEdUTyxUaGFpY29tLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxNC0wNC0xOCwxOToyNTowMCxGOSB2MS4xLENDQUZTIExDLTQwLFNwYWNlWCBDUlMtMywyMjk2LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsQ29udHJvbGxlZCAob2NlYW4pDQoyMDE0LTA3LTE0LDE1OjE1OjAwLEY5IHYxLjEsQ0NBRlMgTEMtNDAsT0cyIE1pc3Npb24gMSAgNiBPcmJjb21tLU9HMiBzYXRlbGxpdGVzLDEzMTYsTEVPLE9yYmNvbW0sU3VjY2VzcyxDb250cm9sbGVkIChvY2VhbikNCjIwMTQtMDgtMDUsODowMDowMCxGOSB2MS4xLENDQUZTIExDLTQwLEFzaWFTYXQgOCw0NTM1LEdUTyxBc2lhU2F0LFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxNC0wOS0wNyw1OjAwOjAwLEY5IHYxLjEgQjEwMTEsQ0NBRlMgTEMtNDAsQXNpYVNhdCA2LDQ0MjgsR1RPLEFzaWFTYXQsU3VjY2VzcyxObyBhdHRlbXB0DQoyMDE0LTA5LTIxLDU6NTI6MDAsRjkgdjEuMSBCMTAxMCxDQ0FGUyBMQy00MCxTcGFjZVggQ1JTLTQsMjIxNixMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLFVuY29udHJvbGxlZCAob2NlYW4pDQoyMDE1LTAxLTEwLDk6NDc6MDAsRjkgdjEuMSBCMTAxMixDQ0FGUyBMQy00MCxTcGFjZVggQ1JTLTUsMjM5NSxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLEZhaWx1cmUgKGRyb25lIHNoaXApDQoyMDE1LTAyLTExLDIzOjAzOjAwLEY5IHYxLjEgQjEwMTMsQ0NBRlMgTEMtNDAsRFNDT1ZSLDU3MCxIRU8sVS5TLiBBaXIgRm9yY2UgTkFTQSBOT0FBLFN1Y2Nlc3MsQ29udHJvbGxlZCAob2NlYW4pDQoyMDE1LTAzLTAyLDM6NTA6MDAsRjkgdjEuMSBCMTAxNCxDQ0FGUyBMQy00MCxBQlMtM0EgRXV0ZWxzYXQgMTE1IFdlc3QgQiw0MTU5LEdUTyxBQlMgRXV0ZWxzYXQsU3VjY2VzcyxObyBhdHRlbXB0DQoyMDE1LTA0LTE0LDIwOjEwOjAwLEY5IHYxLjEgQjEwMTUsQ0NBRlMgTEMtNDAsU3BhY2VYIENSUy02LDE4OTgsTEVPIChJU1MpLE5BU0EgKENSUyksU3VjY2VzcyxGYWlsdXJlIChkcm9uZSBzaGlwKQ0KMjAxNS0wNC0yNywyMzowMzowMCxGOSB2MS4xIEIxMDE2LENDQUZTIExDLTQwLFR1cmttZW4gNTIgLyBNb25hY29TQVQsNDcwNyxHVE8sVHVya21lbmlzdGFuIE5hdGlvbmFsIFNwYWNlIEFnZW5jeSxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTUtMDYtMjgsMTQ6MjE6MDAsRjkgdjEuMSBCMTAxOCxDQ0FGUyBMQy00MCxTcGFjZVggQ1JTLTcsMTk1MixMRU8gKElTUyksTkFTQSAoQ1JTKSxGYWlsdXJlIChpbiBmbGlnaHQpLFByZWNsdWRlZCAoZHJvbmUgc2hpcCkNCjIwMTUtMTItMjIsMToyOTowMCxGOSBGVCBCMTAxOSxDQ0FGUyBMQy00MCxPRzIgTWlzc2lvbiAyICAxMSBPcmJjb21tLU9HMiBzYXRlbGxpdGVzLDIwMzQsTEVPLE9yYmNvbW0sU3VjY2VzcyxTdWNjZXNzIChncm91bmQgcGFkKQ0KMjAxNi0wMS0xNywxODo0MjowMCxGOSB2MS4xIEIxMDE3LFZBRkIgU0xDLTRFLEphc29uLTMsNTUzLExFTyxOQVNBIChMU1ApIE5PQUEgQ05FUyxTdWNjZXNzLEZhaWx1cmUgKGRyb25lIHNoaXApDQoyMDE2LTAzLTA0LDIzOjM1OjAwLEY5IEZUIEIxMDIwLENDQUZTIExDLTQwLFNFUy05LDUyNzEsR1RPLFNFUyxTdWNjZXNzLEZhaWx1cmUgKGRyb25lIHNoaXApDQoyMDE2LTA0LTA4LDIwOjQzOjAwLEY5IEZUIEIxMDIxLjEsQ0NBRlMgTEMtNDAsU3BhY2VYIENSUy04LDMxMzYsTEVPIChJU1MpLE5BU0EgKENSUyksU3VjY2VzcyxTdWNjZXNzIChkcm9uZSBzaGlwKQ0KMjAxNi0wNS0wNiw1OjIxOjAwLEY5IEZUIEIxMDIyLENDQUZTIExDLTQwLEpDU0FULTE0LDQ2OTYsR1RPLFNLWSBQZXJmZWN0IEpTQVQgR3JvdXAsU3VjY2VzcyxTdWNjZXNzIChkcm9uZSBzaGlwKQ0KMjAxNi0wNS0yNywyMTozOTowMCxGOSBGVCBCMTAyMy4xLENDQUZTIExDLTQwLFRoYWljb20gOCwzMTAwLEdUTyxUaGFpY29tLFN1Y2Nlc3MsU3VjY2VzcyAoZHJvbmUgc2hpcCkNCjIwMTYtMDYtMTUsMTQ6Mjk6MDAsRjkgRlQgQjEwMjQsQ0NBRlMgTEMtNDAsQUJTLTJBIEV1dGVsc2F0IDExNyBXZXN0IEIsMzYwMCxHVE8sQUJTIEV1dGVsc2F0LFN1Y2Nlc3MsRmFpbHVyZSAoZHJvbmUgc2hpcCkNCjIwMTYtMDctMTgsNDo0NTowMCxGOSBGVCBCMTAyNS4xLENDQUZTIExDLTQwLFNwYWNlWCBDUlMtOSwyMjU3LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2VzcyAoZ3JvdW5kIHBhZCkNCjIwMTYtMDgtMTQsNToyNjowMCxGOSBGVCBCMTAyNixDQ0FGUyBMQy00MCxKQ1NBVC0xNiw0NjAwLEdUTyxTS1kgUGVyZmVjdCBKU0FUIEdyb3VwLFN1Y2Nlc3MsU3VjY2VzcyAoZHJvbmUgc2hpcCkNCjIwMTctMDEtMTQsMTc6NTQ6MDAsRjkgRlQgQjEwMjkuMSxWQUZCIFNMQy00RSxJcmlkaXVtIE5FWFQgMSw5NjAwLFBvbGFyIExFTyxJcmlkaXVtIENvbW11bmljYXRpb25zLFN1Y2Nlc3MsU3VjY2VzcyAoZHJvbmUgc2hpcCkNCjIwMTctMDItMTksMTQ6Mzk6MDAsRjkgRlQgQjEwMzEuMSxLU0MgTEMtMzlBLFNwYWNlWCBDUlMtMTAsMjQ5MCxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLFN1Y2Nlc3MgKGdyb3VuZCBwYWQpDQoyMDE3LTAzLTE2LDY6MDA6MDAsRjkgRlQgQjEwMzAsS1NDIExDLTM5QSxFY2hvU3RhciAyMyw1NjAwLEdUTyxFY2hvU3RhcixTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTctMDMtMzAsMjI6Mjc6MDAsRjkgRlQgIEIxMDIxLjIsS1NDIExDLTM5QSxTRVMtMTAsNTMwMCxHVE8sU0VTLFN1Y2Nlc3MsU3VjY2VzcyAoZHJvbmUgc2hpcCkNCjIwMTctMDUtMDEsMTE6MTU6MDAsRjkgRlQgQjEwMzIuMSxLU0MgTEMtMzlBLE5ST0wtNzYsNTMwMCxMRU8sTlJPLFN1Y2Nlc3MsU3VjY2VzcyAoZ3JvdW5kIHBhZCkNCjIwMTctMDUtMTUsMjM6MjE6MDAsRjkgRlQgQjEwMzQsS1NDIExDLTM5QSxJbm1hcnNhdC01IEY0LDYwNzAsR1RPLElubWFyc2F0LFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxNy0wNi0wMywyMTowNzowMCxGOSBGVCBCMTAzNS4xLEtTQyBMQy0zOUEsU3BhY2VYIENSUy0xMSwyNzA4LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2VzcyAoZ3JvdW5kIHBhZCkNCjIwMTctMDYtMjMsMTk6MTA6MDAsRjkgRlQgIEIxMDI5LjIsS1NDIExDLTM5QSxCdWxnYXJpYVNhdC0xLDM2NjksR1RPLEJ1bHNhdGNvbSxTdWNjZXNzLFN1Y2Nlc3MgKGRyb25lIHNoaXApDQoyMDE3LTA2LTI1LDIwOjI1OjAwLEY5IEZUIEIxMDM2LjEsVkFGQiBTTEMtNEUsSXJpZGl1bSBORVhUIDIsOTYwMCxMRU8sSXJpZGl1bSBDb21tdW5pY2F0aW9ucyxTdWNjZXNzLFN1Y2Nlc3MgKGRyb25lIHNoaXApDQoyMDE3LTA3LTA1LDIzOjM4OjAwLEY5IEZUIEIxMDM3LEtTQyBMQy0zOUEsSW50ZWxzYXQgMzVlLDY3NjEsR1RPLEludGVsc2F0LFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxNy0wOC0xNCwxNjozMTowMCxGOSBCNCBCMTAzOS4xLEtTQyBMQy0zOUEsU3BhY2VYIENSUy0xMiwzMzEwLExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2VzcyAoZ3JvdW5kIHBhZCkNCjIwMTctMDgtMjQsMTg6NTE6MDAsRjkgRlQgQjEwMzguMSxWQUZCIFNMQy00RSxGb3Jtb3NhdC01LDQ3NSxTU08sTlNQTyxTdWNjZXNzLFN1Y2Nlc3MgKGRyb25lIHNoaXApDQoyMDE3LTA5LTA3LDE0OjAwOjAwLEY5IEI0IEIxMDQwLjEsS1NDIExDLTM5QSxCb2VpbmcgWC0zN0IgT1RWLTUsNDk5MCxMRU8sVS5TLiBBaXIgRm9yY2UsU3VjY2VzcyxTdWNjZXNzIChncm91bmQgcGFkKQ0KMjAxNy0xMC0wOSwxMjozNzowMCxGOSBCNCBCMTA0MS4xLFZBRkIgU0xDLTRFLElyaWRpdW0gTkVYVCAzLDk2MDAsUG9sYXIgTEVPLElyaWRpdW0gQ29tbXVuaWNhdGlvbnMsU3VjY2VzcyxTdWNjZXNzIChkcm9uZSBzaGlwKQ0KMjAxNy0xMC0xMSwyMjo1MzowMCxGOSBGVCAgQjEwMzEuMixLU0MgTEMtMzlBLFNFUy0xMSAvIEVjaG9TdGFyIDEwNSw1MjAwLEdUTyxTRVMgRWNob1N0YXIsU3VjY2VzcyxTdWNjZXNzIChkcm9uZSBzaGlwKQ0KMjAxNy0xMC0zMCwxOTozNDowMCxGOSBCNCBCMTA0Mi4xLEtTQyBMQy0zOUEsS29yZWFzYXQgNUEsMzUwMCxHVE8sS1QgQ29ycG9yYXRpb24sU3VjY2VzcyxTdWNjZXNzIChkcm9uZSBzaGlwKQ0KMjAxNy0xMi0xNSwxNTozNjowMCxGOSBGVCAgQjEwMzUuMixDQ0FGUyBTTEMtNDAsU3BhY2VYIENSUy0xMywyMjA1LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2VzcyAoZ3JvdW5kIHBhZCkNCjIwMTctMTItMjMsMToyNzowMCxGOSBGVCAgQjEwMzYuMixWQUZCIFNMQy00RSxJcmlkaXVtIE5FWFQgNCw5NjAwLFBvbGFyIExFTyxJcmlkaXVtIENvbW11bmljYXRpb25zLFN1Y2Nlc3MsQ29udHJvbGxlZCAob2NlYW4pDQoyMDE4LTAxLTA4LDE6MDA6MDAsRjkgQjQgQjEwNDMuMSxDQ0FGUyBTTEMtNDAsWnVtYSw1MDAwLExFTyxOb3J0aHJvcCBHcnVtbWFuLFN1Y2Nlc3MgKHBheWxvYWQgc3RhdHVzIHVuY2xlYXIpLFN1Y2Nlc3MgKGdyb3VuZCBwYWQpDQoyMDE4LTAxLTMxLDIxOjI1OjAwLEY5IEZUICBCMTAzMi4yLENDQUZTIFNMQy00MCxHb3ZTYXQtMSAvIFNFUy0xNiw0MjMwLEdUTyxTRVMsU3VjY2VzcyxDb250cm9sbGVkIChvY2VhbikNCjIwMTgtMDItMjIsMTQ6MTc6MDAsRjkgRlQgIEIxMDM4LjIsVkFGQiBTTEMtNEUsUGF6ICBUaW50aW4gQSAmIEIsMjE1MCxTU08sSGlzZGVzYXQgZXhhY3RFYXJ0aCBTcGFjZVgsU3VjY2VzcyxObyBhdHRlbXB0DQoyMDE4LTAzLTA2LDU6MzM6MDAsRjkgQjQgQjEwNDQsQ0NBRlMgU0xDLTQwLEhpc3Bhc2F0IDMwVy02ICBQT0RTYXQsNjA5MixHVE8sSGlzcGFzYXQgIE5vdmFXdXJrcyxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTgtMDMtMzAsMTQ6MTQ6MDAsRjkgQjQgIEIxMDQxLjIsVkFGQiBTTEMtNEUsSXJpZGl1bSBORVhUIDUsOTYwMCxQb2xhciBMRU8sSXJpZGl1bSBDb21tdW5pY2F0aW9ucyxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTgtMDQtMDIsMjA6MzA6MDAsRjkgQjQgIEIxMDM5LjIsQ0NBRlMgU0xDLTQwLFNwYWNlWCBDUlMtMTQsMjY0NyxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTgtMDQtMTgsMjI6NTE6MDAsRjkgQjQgQjEwNDUuMSxDQ0FGUyBTTEMtNDAsVHJhbnNpdGluZyBFeG9wbGFuZXQgU3VydmV5IFNhdGVsbGl0ZSAoVEVTUyksMzYyLEhFTyxOQVNBIChMU1ApLFN1Y2Nlc3MsU3VjY2VzcyAoZHJvbmUgc2hpcCkNCjIwMTgtMDUtMTEsMjA6MTQ6MDAsRjkgQjUgIEIxMDQ2LjEsS1NDIExDLTM5QSxCYW5nYWJhbmRodS0xLDM2MDAsR1RPLFRoYWxlcy1BbGVuaWEvQlRSQyxTdWNjZXNzLFN1Y2Nlc3MgKGRyb25lIHNoaXApDQoyMDE4LTA1LTIyLDE5OjQ3OjU4LEY5IEI0ICBCMTA0My4yLFZBRkIgU0xDLTRFLCJJcmlkaXVtIE5FWFQgNiAgIEdSQUNFLUZPIDEsIDIiLDY0NjAsUG9sYXIgTEVPLElyaWRpdW0gQ29tbXVuaWNhdGlvbnMgR0ZaIOKAmiBOQVNBLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxOC0wNi0wNCw0OjQ1OjAwLEY5IEI0ICBCMTA0MC4yLENDQUZTIFNMQy00MCxTRVMtMTIsNTM4NCxHVE8sU0VTLFN1Y2Nlc3MsTm8gYXR0ZW1wdA0KMjAxOC0wNi0yOSw5OjQyOjAwLEY5IEI0IEIxMDQ1LjIsQ0NBRlMgU0xDLTQwLFNwYWNlWCBDUlMtMTUsMjY5NyxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMTgtMDctMjIsNTo1MDowMCxGOSBCNUIxMDQ3LjEsQ0NBRlMgU0xDLTQwLFRlbHN0YXIgMTlWLDcwNzUsR1RPLFRlbGVzYXQsU3VjY2VzcyxTdWNjZXNzDQoyMDE4LTA3LTI1LDExOjM5OjAwLEY5IEI1QjEwNDguMSxWQUZCIFNMQy00RSxJcmlkaXVtIE5FWFQtNyw5NjAwLFBvbGFyIExFTyxJcmlkaXVtIENvbW11bmljYXRpb25zLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOC0wOC0wNyw1OjE4OjAwLEY5IEI1IEIxMDQ2LjIsQ0NBRlMgU0xDLTQwLE1lcmFoIFB1dGloICw1ODAwLEdUTyxUZWxrb20gSW5kb25lc2lhLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOC0wOS0xMCw0OjQ1OjAwLEY5IEI1QjEwNDkuMSxDQ0FGUyBTTEMtNDAsVGVsc3RhciAxOFYgLyBBcHN0YXItNUMsNzA2MCxHVE8sVGVsZXNhdCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMTgtMTAtMDgsMjoyMjowMCxGOSBCNSBCMTA0OC4yLFZBRkIgU0xDLTRFLFNBT0NPTSAxQSwzMDAwLFNTTyxDT05BRSxTdWNjZXNzLFN1Y2Nlc3MNCjIwMTgtMTEtMTUsMjA6NDY6MDAsRjkgQjUgQjEwNDcuMixLU0MgTEMtMzlBLEVzIGhhaWwgMiw1MzAwLEdUTyxFcyBoYWlsU2F0LFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOC0xMi0wMywxODozNDowNSxGOSBCNSBCMTA0Ni4zLFZBRkIgU0xDLTRFLFNTTy1BICw0MDAwLFNTTyxTcGFjZWZsaWdodCBJbmR1c3RyaWVzLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOC0xMi0wNSwxODoxNjowMCxGOSBCNUIxMDUwLENDQUZTIFNMQy00MCxTcGFjZVggQ1JTLTE2LDI1MDAsTEVPIChJU1MpLE5BU0EgKENSUyksU3VjY2VzcyxGYWlsdXJlDQoyMDE4LTEyLTIzLDEzOjUxOjAwLEY5IEI1QjEwNTQsQ0NBRlMgU0xDLTQwLEdQUyBJSUktMDEgLDQ0MDAsTUVPLFVTQUYsU3VjY2VzcyAsTm8gYXR0ZW1wdA0KMjAxOS0wMS0xMSwxNTozMTowMCxGOSBCNSBCMTA0OS4yLFZBRkIgU0xDLTRFLElyaWRpdW0gTkVYVC04LDk2MDAsUG9sYXIgTEVPLElyaWRpdW0gQ29tbXVuaWNhdGlvbnMsU3VjY2VzcyxTdWNjZXNzDQoyMDE5LTAyLTIyLDE6NDU6MDAsRjkgQjUgQjEwNDguMyxDQ0FGUyBTTEMtNDAsIk51c2FudGFyYSBTYXR1LCBCZXJlc2hlZXQgTW9vbiBsYW5kZXIsIFM1Iiw0ODUwLEdUTywiUFNOLCBTcGFjZUlMIC8gSUFJIixTdWNjZXNzLFN1Y2Nlc3MNCjIwMTktMDMtMDIsNzo0OTowMCxGOSBCNUIxMDUxLjEsS1NDIExDLTM5QSwiQ3JldyBEcmFnb24gRGVtby0xLCBTcGFjZVggQ1JTLTE3ICIsMTIwNTUsTEVPIChJU1MpLE5BU0EgKENDRCkgLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOS0wNS0wNCw2OjQ4OjAwLEY5IEI1QjEwNTYuMSAsQ0NBRlMgU0xDLTQwLCJTcGFjZVggQ1JTLTE3LCBTdGFybGluayB2MC45IiwyNDk1LExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOS0wNS0yNCwyOjMwOjAwLEY5IEI1IEIxMDQ5LjMsQ0NBRlMgU0xDLTQwLCJTdGFybGluayB2MC45LCBSQURBUlNBVCBDb25zdGVsbGF0aW9uIiwxMzYyMCxMRU8sU3BhY2VYLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOS0wNi0xMiwxNDoxNzowMCxGOSBCNSBCMTA1MS4yICxWQUZCIFNMQy00RSwiUkFEQVJTQVQgQ29uc3RlbGxhdGlvbiwgU3BhY2VYIENSUy0xOCAiLDQyMDAsU1NPLENhbmFkaWFuIFNwYWNlIEFnZW5jeSAoQ1NBKSxTdWNjZXNzLFN1Y2Nlc3MNCjIwMTktMDctMjUsMjI6MDE6MDAsRjkgQjUgQjEwNTYuMiAsQ0NBRlMgU0xDLTQwLCJTcGFjZVggQ1JTLTE4LCBBTU9TLTE3ICIsMjI2OCxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLFN1Y2Nlc3MNCjIwMTktMDgtMDYsMjM6MjM6MDAsRjkgQjUgQjEwNDcuMyAsQ0NBRlMgU0xDLTQwLCJBTU9TLTE3LCBTdGFybGluayAxIHYxLjAgIiw2NTAwLEdUTyxTcGFjZWNvbSxTdWNjZXNzLE5vIGF0dGVtcHQgDQoyMDE5LTExLTExLDE0OjU2OjAwLEY5IEI1IEIxMDQ4LjQsQ0NBRlMgU0xDLTQwLCJTdGFybGluayAxIHYxLjAsIFNwYWNlWCBDUlMtMTkgIiwxNTYwMCxMRU8sU3BhY2VYLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOS0xMi0wNSwxNzoyOTowMCxGOSBCNUIxMDU5LjEsQ0NBRlMgU0xDLTQwLCJTcGFjZVggQ1JTLTE5LCBKQ1NhdC0xOCAvIEthY2lmaWMgMSAiLDI2MTcsTEVPIChJU1MpLCJOQVNBIChDUlMpLCBLYWNpZmljIDEiLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAxOS0xMi0xNywwOjEwOjAwLEY5IEI1IEIxMDU2LjMgLENDQUZTIFNMQy00MCwiSkNTYXQtMTggLyBLYWNpZmljIDEsIFN0YXJsaW5rIDIgdjEuMCAiLDY5NTYsR1RPLCJTa3kgUGVyZmVjdCBKU0FULCBLYWNpZmljIDEiLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAyMC0wMS0wNywyOjMzOjAwLEY5IEI1IEIxMDQ5LjQsQ0NBRlMgU0xDLTQwLCJTdGFybGluayAyIHYxLjAsIENyZXcgRHJhZ29uIGluLWZsaWdodCBhYm9ydCB0ZXN0ICIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMDEtMTksMTU6MzA6MDAsRjkgQjUgQjEwNDYuNCxLU0MgTEMtMzlBLCJDcmV3IERyYWdvbiBpbi1mbGlnaHQgYWJvcnQgdGVzdCwgU3RhcmxpbmsgMyB2MS4wICIsMTIwNTAsU3ViLW9yYml0YWwsTkFTQSAoQ1RTKSxTdWNjZXNzLE5vIGF0dGVtcHQNCjIwMjAtMDEtMjksMTQ6MDc6MDAsRjkgQjUgQjEwNTEuMyxDQ0FGUyBTTEMtNDAsIlN0YXJsaW5rIDMgdjEuMCwgU3RhcmxpbmsgNCB2MS4wICIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMDItMTcsMTU6MDU6MDAsRjkgQjUgQjEwNTYuNCxDQ0FGUyBTTEMtNDAsIlN0YXJsaW5rIDQgdjEuMCwgU3BhY2VYIENSUy0yMCIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLEZhaWx1cmUNCjIwMjAtMDMtMDcsNDo1MDowMCxGOSBCNSBCMTA1OS4yLENDQUZTIFNMQy00MCwiU3BhY2VYIENSUy0yMCwgU3RhcmxpbmsgNSB2MS4wICIsMTk3NyxMRU8gKElTUyksTkFTQSAoQ1JTKSxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMDMtMTgsMTI6MTY6MDAsRjkgQjUgQjEwNDguNSxLU0MgTEMtMzlBLCJTdGFybGluayA1IHYxLjAsIFN0YXJsaW5rIDYgdjEuMCAiLDE1NjAwLExFTyxTcGFjZVgsU3VjY2VzcyxGYWlsdXJlDQoyMDIwLTA0LTIyLDE5OjMwOjAwLEY5IEI1IEIxMDUxLjQsS1NDIExDLTM5QSwiU3RhcmxpbmsgNiB2MS4wLCBDcmV3IERyYWdvbiBEZW1vLTIgIiwxNTYwMCxMRU8sU3BhY2VYLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAyMC0wNS0zMCwxOToyMjowMCxGOSBCNUIxMDU4LjEgLEtTQyBMQy0zOUEsIkNyZXcgRHJhZ29uIERlbW8tMiwgU3RhcmxpbmsgNyB2MS4wICIsMTI1MzAsTEVPIChJU1MpLE5BU0EgKENDRGV2KSxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMDYtMDQsMToyNTowMCxGOSBCNSBCMTA0OS41LENDQUZTIFNMQy00MCwiU3RhcmxpbmsgNyB2MS4wLCBTdGFybGluayA4IHYxLjAiLDE1NjAwLExFTywiU3BhY2VYLCBQbGFuZXQgTGFicyIsU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTA2LTEzLDk6MjE6MDAsRjkgQjUgQjEwNTkuMyxDQ0FGUyBTTEMtNDAsIlN0YXJsaW5rIDggdjEuMCwgU2t5U2F0cy0xNiwgLTE3LCAtMTgsIEdQUyBJSUktMDMgIiwxNTQxMCxMRU8sIlNwYWNlWCwgUGxhbmV0IExhYnMiLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAyMC0wNi0zMCwyMDoxMDo0NixGOSBCNUIxMDYwLjEsQ0NBRlMgU0xDLTQwLCJHUFMgSUlJLTAzLCBBTkFTSVMtSUkiLDQzMTEsTUVPLFUuUy4gU3BhY2UgRm9yY2UsU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTA3LTIwLDIxOjMwOjAwLEY5IEI1IEIxMDU4LjIgLENDQUZTIFNMQy00MCwiQU5BU0lTLUlJLCBTdGFybGluayA5IHYxLjAiLDU1MDAsR1RPLCJSZXB1YmxpYyBvZiBLb3JlYSBBcm15LCBTcGFjZWZsaWdodCBJbmR1c3RyaWVzIChCbGFja1NreSkiLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAyMC0wOC0wNyw1OjEyOjAwLEY5IEI1IEIxMDUxLjUsS1NDIExDLTM5QSwiU3RhcmxpbmsgOSB2MS4wLCBTWFJTLTEsIFN0YXJsaW5rIDEwIHYxLjAgIiwxNDkzMixMRU8sIlNwYWNlWCwgU3BhY2VmbGlnaHQgSW5kdXN0cmllcyAoQmxhY2tTa3kpLCBQbGFuZXQgTGFicyIsU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTA4LTE4LDE0OjMxOjAwLEY5IEI1IEIxMDQ5LjYsQ0NBRlMgU0xDLTQwLCJTdGFybGluayAxMCB2MS4wLCBTa3lTYXQtMTksIC0yMCwgLTIxLCBTQU9DT00gMUIgIiwxNTQ0MCxMRU8sIlNwYWNlWCwgUGxhbmV0IExhYnMsIFBsYW5ldElRIixTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMDgtMzAsMjM6MTg6MDAsRjkgQjUgQjEwNTkuNCxDQ0FGUyBTTEMtNDAsIlNBT0NPTSAxQiwgR05PTUVTIDEsIFR5dmFrLTAxNzIiLDMxMzAsU1NPLCJDT05BRSwgUGxhbmV0SVEsIFNwYWNlWCIsU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTA5LTAzLDEyOjQ2OjE0LEY5IEI1IEIxMDYwLjIgLEtTQyBMQy0zOUEsIlN0YXJsaW5rIDExIHYxLjAsIFN0YXJsaW5rIDEyIHYxLjAgIiwxNTYwMCxMRU8sU3BhY2VYLFN1Y2Nlc3MsU3VjY2Vzcw0KMjAyMC0xMC0wNiwxMToyOTozNCxGOSBCNSBCMTA1OC4zICxLU0MgTEMtMzlBLCJTdGFybGluayAxMiB2MS4wLCBTdGFybGluayAxMyB2MS4wICIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMTAtMTgsMTI6MjU6NTcsRjkgQjUgQjEwNTEuNixLU0MgTEMtMzlBLCJTdGFybGluayAxMyB2MS4wLCBTdGFybGluayAxNCB2MS4wICIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMTAtMjQsMTU6MzE6MzQsRjkgQjUgQjEwNjAuMyxDQ0FGUyBTTEMtNDAsIlN0YXJsaW5rIDE0IHYxLjAsIEdQUyBJSUktMDQgICIsMTU2MDAsTEVPLFNwYWNlWCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMTEtMDUsMjM6MjQ6MjMsRjkgQjVCMTA2Mi4xLENDQUZTIFNMQy00MCwiR1BTIElJSS0wNCAsIENyZXctMSIsNDMxMSxNRU8sVVNTRixTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMTEtMTYsMDoyNzowMCxGOSBCNUIxMDYxLjEgLEtTQyBMQy0zOUEsIkNyZXctMSwgU2VudGluZWwtNiBNaWNoYWVsIEZyZWlsaWNoICIsMTI1MDAsTEVPIChJU1MpLE5BU0EgKENDUCksU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTExLTIxLDE3OjE3OjA4LEY5IEI1QjEwNjMuMSxWQUZCIFNMQy00RSwiU2VudGluZWwtNiBNaWNoYWVsIEZyZWlsaWNoLCBTdGFybGluayAxNSB2MS4wICIsMTE5MixMRU8sTkFTQSAvIE5PQUEgLyBFU0EgLyBFVU1FVFNBVCxTdWNjZXNzLFN1Y2Nlc3MNCjIwMjAtMTEtMjUsMjoxMzowMCxGOSBCNSBCMTA0OS43ICxDQ0FGUyBTTEMtNDAsIlN0YXJsaW5rIDE1IHYxLjAsIFNwYWNlWCBDUlMtMjEiLDE1NjAwLExFTyxTcGFjZVgsU3VjY2VzcyxTdWNjZXNzDQoyMDIwLTEyLTA2LDE2OjE3OjA4LEY5IEI1IEIxMDU4LjQgLEtTQyBMQy0zOUEsU3BhY2VYIENSUy0yMSwyOTcyLExFTyAoSVNTKSxOQVNBIChDUlMpLFN1Y2Nlc3MsU3VjY2Vzcw0K)
"""

!pip install sqlalchemy==1.3.9

"""Connect to the database
Let us first load the SQL extension and establish a connection with the database
"""

#Please uncomment and execute the code below if you are working locally.
!pip install ipython-sql

# Commented out IPython magic to ensure Python compatibility.
# %load_ext sql

import csv, sqlite3
con = sqlite3.connect("my_data1.db")
cur = con.cursor()

!pip install -q pandas

# Commented out IPython magic to ensure Python compatibility.
# %sql sqlite:///my_data1.db

import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")

"""Note:This below code is added to remove blank rows from table"""

# Commented out IPython magic to ensure Python compatibility.
# %sql create table SPACEXTABLE as select * from SPACEXTBL where Date is not null

"""# Tasks
Now write and execute SQL queries to solve the assignment tasks.

Note: If the column names are in mixed case enclose it in double quotes For Example "Landing_Outcome"

# Task 1
Display the names of the unique launch sites in the space mission
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select distinct Launch_site from SPACEXTBL

"""# Task 2
Display 5 records where launch sites begin with the string 'CCA'
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select * from SPACEXTBL where Launch_site like 'CCA%' limit 5

"""# Task 3
Display the total payload mass carried by boosters launched by NASA (CRS)
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT SUM(PAYLOAD_MASS__KG_) || ' kg' AS Total_Payload_Mass FROM SPACEXTBL WHERE Customer = 'NASA (CRS)';

"""# Task 4
Display average payload mass carried by booster version F9 v1.1
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select avg(PAYLOAD_MASS__KG_)  || ' kg'as Average_Payload_Mass from SPACEXTBL where Booster_Version like 'F9 v1.1'

"""# Task 5
List the date when the first succesful landing outcome in ground pad was acheived.
Hint:Use min function
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select min(Date) as First_Successful_Landing_Date from SPACEXTBL where Landing_Outcome = 'Success (ground pad)'

"""# Task 6
List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select Booster_Version,PAYLOAD_MASS__KG_ , 'Success (drone ship)' from SPACEXTBL where Landing_Outcome = 'Success (drone ship)' and PAYLOAD_MASS__KG_ between 4000 and 6000

"""# Task 7
List the total number of successful and failure mission outcomes
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT Count(Mission_Outcome) as The_Number_Of_Mission_Outcomes, Mission_Outcome from SPACEXTBL group by Mission_Outcome order by Mission_Outcome

"""# Task 8
List the names of the booster_versions which have carried the maximum payload mass. Use a subquery
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql select Booster_Version, PAYLOAD_MASS__KG_ from SPACEXTBL where PAYLOAD_MASS__KG_ like (select MAX(PAYLOAD_MASS__KG_) from SPACEXTBL) ORDER BY booster_version;

"""# Task 9
List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
Note: SQLLite does not support monthnames. So you need to use substr(Date, 6,2) as month to get the months and substr(Date,0,5)='2015' for year.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT
#     CASE SUBSTR(Date, 6, 2)
#         WHEN '01' THEN 'January'
#         WHEN '02' THEN 'February'
#         WHEN '03' THEN 'March'
#         WHEN '04' THEN 'April'
#         WHEN '05' THEN 'May'
#         WHEN '06' THEN 'June'
#         WHEN '07' THEN 'July'
#         WHEN '08' THEN 'August'
#         WHEN '09' THEN 'September'
#         WHEN '10' THEN 'October'
#         WHEN '11' THEN 'November'
#         WHEN '12' THEN 'December'
#     END AS Month,
#     Landing_Outcome,
#     Booster_Version,
#     Launch_Site
# FROM
#     SPACEXTBL
# WHERE
#     Landing_Outcome = 'Failure (drone ship)'
#     AND SUBSTR(Date,0,5) = '2015';

"""# Task 10
Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order.
"""

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT Landing_Outcome, COUNT(landing_outcome) AS Count, DATE FROM SPACEXTBL WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY Landing_Outcome ORDER BY Count DESC;