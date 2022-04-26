# Tiktok-AutoClaimer

Tiktok Username Claimer/Sniper

1. Run Tiktok_Claimer.py
2. Enter username to claim
3. Enter sid of account that will check avalibility of the username. (Do not use account sid that you will claim on if checking for long periods of time. (This is to avoid rate limits.))
4. Enter the sid (session id) of the account you want to claim username to.
5. Enter tt_csrf_token of the account you want to claim to.


Instructions (To get your sid and tt_csrf_token)

1. Add Cookie editor to chrome. (https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
2. Go to tiktok.com and click on cookie editor on your extentions bar.
3. Find sid and tt_csrf_token and copy and paste the values.

Requierments
1. pip install threading

Future Updates:
1. Will add the choice of using proxys
2. Autogenerate checking sid
3. Fix Error that states the autoclaim failed when it actually didnt

Ratelimits

1. Due to not being able to use proxys (at this time) whilst checking, I recomend not to run the checker for more than 20 seconds at a time.
