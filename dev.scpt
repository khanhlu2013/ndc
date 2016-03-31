tell application "Terminal" to do script "cd ~/lu/ndc-ng2; npm run _start_django_server"
tell application "Terminal" to do script "cd ~/lu/ndc-ng2; npm run _compile_ts_n_watch_2_refresh_browser"
tell application "Terminal" to do script "cd ~/lu/ndc-ng2; npm run _test_develop_n_watch"


tell application "Terminal"
    repeat with w from 1 to count windows
        repeat with t from 1 to count tabs of window w
            set current settings of tab t of window w to (first settings set whose name is "Homebrew")
        end repeat
    end repeat
end tell