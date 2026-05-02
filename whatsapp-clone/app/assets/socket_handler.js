// Auto-scroll messages to bottom whenever the messages container changes
var scrollObserver = new MutationObserver(function(mutations) {
    var scrollArea = document.getElementById('messages-scroll');
    if (scrollArea) {
        scrollArea.scrollTop = scrollArea.scrollHeight;
    }
});

function watchMessages() {
    var container = document.getElementById('messages-container');
    if (container) {
        scrollObserver.observe(container, { childList: true, subtree: true });
        var scrollArea = document.getElementById('messages-scroll');
        if (scrollArea) {
            scrollArea.scrollTop = scrollArea.scrollHeight;
        }
    } else {
        setTimeout(watchMessages, 500);
    }
}

// Start watching
watchMessages();

// Re-watch whenever the DOM changes significantly (SPA navigation)
var pageObserver = new MutationObserver(function(mutations) {
    for (var i = 0; i < mutations.length; i++) {
        if (mutations[i].addedNodes.length > 0) {
            watchMessages();
            break;
        }
    }
});

window.addEventListener('load', function() {
    var pageContent = document.getElementById('page-content');
    if (pageContent) {
        pageObserver.observe(pageContent, { childList: true, subtree: false });
    }
    setTimeout(watchMessages, 1000);
});

// Enter key to send message (without Shift for newline)
document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        var msgInput = document.getElementById('message-input');
        if (msgInput && document.activeElement === msgInput) {
            e.preventDefault();
            var sendBtn = document.getElementById('send-btn');
            if (sendBtn) {
                sendBtn.click();
            }
        }
    }
});

// Auto-select OTP input text on focus for easy replacement
document.addEventListener('focus', function(e) {
    if (e.target && e.target.id === 'otp-input') {
        e.target.select();
    }
}, true);
