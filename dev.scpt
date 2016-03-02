tell application "Terminal" to do script "source ./lu/ndc-ng2/venv/bin/activate;foreman start --procfile ./lu/ndc-ng2/Procfile_local --env ./lu/ndc-ng2/.env"

tell application "Terminal"
    repeat with w from 1 to count windows
        repeat with t from 1 to count tabs of window w
            set current settings of tab t of window w to (first settings set whose name is "Homebrew")
        end repeat
    end repeat
end tell