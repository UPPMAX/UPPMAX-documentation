document.addEventListener("DOMContentLoaded", function () {
    var script = document.createElement("script");
    script.type = "module";
    script.id = "runllm-widget-script"
  
    script.src = "https://widget.runllm.com";
  
    script.setAttribute("version", "stable");
    script.setAttribute("crossorigin", "true");
    script.setAttribute("runllm-keyboard-shortcut", "Mod+j");
    script.setAttribute("runllm-name", "UPPMAX AI Assistant");
    script.setAttribute("runllm-position", "BOTTOM_RIGHT");
    script.setAttribute("runllm-assistant-id", "733");
    script.setAttribute("runllm-disable-ask-a-person", "true");
    script.setAttribute("runllm-per-user-usage-limit", "3");
    script.setAttribute("runllm-disclaimer", "This is AI assistant is in development and may not always provide accurate information.");
  
    script.async = true;
    document.head.appendChild(script);
  });