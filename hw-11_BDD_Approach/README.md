Tests from hw-11_BDD_Approach folder were created for testing CRUD user via UI and API. Before running read following infomation: 
1. Go to the folder hw-11_BDD_Approach(for example: "C:\Automation\hw-11_BDD_Approach")
2. For running tests by labels use following commands in the terminal:
   - All UI and API tests use: pytest ./steps -m "webtest or apitest"
   - ONLY API tests use: pytest ./steps -m apitest
   - ONLY UI test use: pytest ./steps -m webtest