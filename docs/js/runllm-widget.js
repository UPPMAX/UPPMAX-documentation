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
    script.setAttribute("runllm-usage-limit-effective-days", "1");
    script.setAttribute("runllm-usage-limit-message", "There is a usage limit set at 3 queries per day, since this Assisstant is in development. This limit resets in 1 day, please try again tomorrow.");
  
    script.async = true;
    document.head.appendChild(script);
  });