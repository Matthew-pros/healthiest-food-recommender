#!/bin/bash
mkdir -p ~/.streamlit/
echo "\n[server]\n\nheadless = true\n\nport = $PORT\n\nenableCORS = false\n\n" > ~/.streamlit/config.toml
