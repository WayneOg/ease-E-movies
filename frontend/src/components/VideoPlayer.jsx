import { useState, useEffect, useRef, useMemo } from 'react';
import { FiX, FiServer, FiChevronDown } from 'react-icons/fi';

const VideoPlayer = ({ wootlyUrl, doodUrl, title, onClose, movieId, type = 'movie', seasonNumber, episodeNumber }) => {
  const iframeRef = useRef(null);
  
  // Generate multiple VidSrc URLs as alternatives
  const vidsrcUrls = useMemo(() => {
    if (!movieId) return {};
    
    const generateUrl = (domain) => {
      if (type === 'tv' && seasonNumber && episodeNumber) {
        return `https://${domain}/embed/tv/${movieId}/${seasonNumber}/${episodeNumber}`;
      }
      return `https://${domain}/embed/movie/${movieId}`;
    };
    
    const urls = {
      vidsrc1: generateUrl('vidsrc.to'),      // Primary - Most reliable
      vidsrc2: generateUrl('vidsrc.xyz'),     // Alternative 1
      vidsrc3: generateUrl('vidsrc.me'),      // Alternative 2
      vidsrc4: generateUrl('vidsrc.net'),     // Alternative 3
      vidsrc5: generateUrl('vidsrc.cc'),      // Alternative 4
    };
    
    console.log('🎬 Generated VidSrc URLs:', urls);
    return urls;
  }, [movieId, type, seasonNumber, episodeNumber]);
  
  const vidsrcUrl = vidsrcUrls.vidsrc1; // Primary VidSrc URL (vidsrc.to)
  
  // Determine initial source: prefer VidSrc, then custom URLs
  const [selectedSource, setSelectedSource] = useState(() => {
    // Compute VidSrc URL for initial state
    let initialVidsrcUrl = null;
    if (movieId) {
      if (type === 'tv' && seasonNumber && episodeNumber) {
        initialVidsrcUrl = `https://vidsrc.to/embed/tv/${movieId}/${seasonNumber}/${episodeNumber}`;
      } else {
        initialVidsrcUrl = `https://vidsrc.to/embed/movie/${movieId}`;
      }
    }
    
    if (initialVidsrcUrl) return 'vidsrc';
    if (wootlyUrl) return 'wootly';
    if (doodUrl) return 'dood';
    return null;
  });
  const [showServerMenu, setShowServerMenu] = useState(false);

  // Get current URL based on selected source using useMemo
  const currentUrl = useMemo(() => {
    switch (selectedSource) {
      case 'wootly': return wootlyUrl;
      case 'dood': return doodUrl;
      case 'vidsrc': return vidsrcUrl;
      case 'vidsrc2': return vidsrcUrls.vidsrc2;
      case 'vidsrc3': return vidsrcUrls.vidsrc3;
      case 'vidsrc4': return vidsrcUrls.vidsrc4;
      case 'vidsrc5': return vidsrcUrls.vidsrc5;
      default: return vidsrcUrl || wootlyUrl || doodUrl;
    }
  }, [selectedSource, wootlyUrl, doodUrl, vidsrcUrl, vidsrcUrls]);

  // Enhanced Ad Blocker and Popup Blocker
  useEffect(() => {
    console.log('🛡️ Initializing Enhanced Ad Blocker...');
    
    // 1. Block ALL popup windows completely
    const originalWindowOpen = window.open;
    window.open = function(...args) {
      console.log('🚫 Blocked popup attempt:', args);
      return null;
    };

    // 2. Block ALL click events that try to open new windows/tabs
    const handleClick = (e) => {
      const target = e.target;
      
      // Block any link with target="_blank"
      const link = target.closest('a');
      if (link && (link.target === '_blank' || link.href)) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('🚫 Blocked link click:', link.href);
        return false;
      }
      
      // Block middle mouse button clicks (open in new tab)
      if (e.button === 1) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('🚫 Blocked middle click');
        return false;
      }
      
      // Block ctrl+click and cmd+click (new tab)
      if (e.ctrlKey || e.metaKey) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('🚫 Blocked ctrl/cmd+click');
        return false;
      }
    };

    // 3. Block mousedown events (catches some ad scripts)
    const handleMouseDown = (e) => {
      if (e.button === 1 || e.ctrlKey || e.metaKey) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('🚫 Blocked mousedown event');
        return false;
      }
    };

    // 4. Block mouseup events (catches more ad scripts)
    const handleMouseUp = (e) => {
      if (e.button === 1 || e.ctrlKey || e.metaKey) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        console.log('🚫 Blocked mouseup event');
        return false;
      }
    };

    // 5. Block context menu (right-click)
    const handleContextMenu = (e) => {
      e.preventDefault();
      e.stopPropagation();
      console.log('🚫 Blocked context menu');
      return false;
    };

    // 6. Block beforeunload redirects
    const handleBeforeUnload = (e) => {
      if (!e.target.closest('.player-close-btn')) {
        e.preventDefault();
        e.returnValue = '';
        console.log('🚫 Blocked beforeunload redirect');
      }
    };

    // 7. Block focus events (some ads use focus to open popups)
    const handleFocus = (e) => {
      if (e.target !== window && e.target !== document) {
        console.log('🚫 Blocked focus event on:', e.target);
      }
    };

    // 8. Override alert, confirm, prompt (some ads use these)
    const originalAlert = window.alert;
    const originalConfirm = window.confirm;
    const originalPrompt = window.prompt;
    
    window.alert = function(...args) {
      console.log('🚫 Blocked alert:', args);
      return undefined;
    };
    
    window.confirm = function(...args) {
      console.log('🚫 Blocked confirm:', args);
      return false;
    };
    
    window.prompt = function(...args) {
      console.log('🚫 Blocked prompt:', args);
      return null;
    };

    // Add event listeners with capture phase (catches events before they bubble)
    document.addEventListener('click', handleClick, true);
    document.addEventListener('mousedown', handleMouseDown, true);
    document.addEventListener('mouseup', handleMouseUp, true);
    document.addEventListener('contextmenu', handleContextMenu, true);
    document.addEventListener('auxclick', handleClick, true); // Middle/right click
    window.addEventListener('beforeunload', handleBeforeUnload, true);
    window.addEventListener('focus', handleFocus, true);

    console.log('✅ Enhanced Ad Blocker Active!');

    // Cleanup
    return () => {
      window.open = originalWindowOpen;
      window.alert = originalAlert;
      window.confirm = originalConfirm;
      window.prompt = originalPrompt;
      document.removeEventListener('click', handleClick, true);
      document.removeEventListener('mousedown', handleMouseDown, true);
      document.removeEventListener('mouseup', handleMouseUp, true);
      document.removeEventListener('contextmenu', handleContextMenu, true);
      document.removeEventListener('auxclick', handleClick, true);
      window.removeEventListener('beforeunload', handleBeforeUnload, true);
      window.removeEventListener('focus', handleFocus, true);
      console.log('🛡️ Ad Blocker Deactivated');
    };
  }, []);

  // Monitor and block iframe redirects + Auto-skip ads
  useEffect(() => {
    console.log('🎯 Starting iframe monitor and ad auto-skipper...');
    
    const checkIframeRedirects = setInterval(() => {
      if (iframeRef.current) {
        try {
          const iframe = iframeRef.current;
          
          // Prevent iframe from navigating parent window
          if (iframe.contentWindow) {
            iframe.contentWindow.onbeforeunload = null;
            
            // Try to access iframe document (will work if same-origin)
            try {
              const iframeDoc = iframe.contentWindow.document;
              
              if (iframeDoc) {
                // 1. Remove ad overlays and popups
                const adSelectors = [
                  '[class*="ad-"]',
                  '[id*="ad-"]',
                  '[class*="popup"]',
                  '[id*="popup"]',
                  '[class*="overlay"]',
                  '[id*="overlay"]',
                  '[class*="banner"]',
                  '[id*="banner"]',
                  '.advertisement',
                  '#advertisement',
                  '[class*="sponsor"]',
                  '[id*="sponsor"]',
                  'iframe[src*="ads"]',
                  'iframe[src*="doubleclick"]',
                  'iframe[src*="googlesyndication"]',
                  'div[style*="z-index: 999"]',
                  'div[style*="z-index: 9999"]',
                ];
                
                adSelectors.forEach(selector => {
                  const elements = iframeDoc.querySelectorAll(selector);
                  elements.forEach(el => {
                    if (el && el.parentNode) {
                      el.remove();
                      console.log('🗑️ Removed ad element:', selector);
                    }
                  });
                });
                
                // 2. Auto-click "Skip Ad" buttons
                const skipButtonSelectors = [
                  'button[class*="skip"]',
                  'button[id*="skip"]',
                  'div[class*="skip"]',
                  'div[id*="skip"]',
                  'a[class*="skip"]',
                  'a[id*="skip"]',
                  '[aria-label*="Skip"]',
                  '[aria-label*="skip"]',
                  'button:contains("Skip")',
                  'button:contains("skip")',
                  '.ytp-ad-skip-button',
                  '.videoAdUiSkipButton',
                ];
                
                skipButtonSelectors.forEach(selector => {
                  const buttons = iframeDoc.querySelectorAll(selector);
                  buttons.forEach(btn => {
                    if (btn && btn.offsetParent !== null) { // Check if visible
                      btn.click();
                      console.log('⏭️ Auto-clicked skip button:', selector);
                    }
                  });
                });
                
                // 3. Remove elements with high z-index (usually overlays)
                const allElements = iframeDoc.querySelectorAll('*');
                allElements.forEach(el => {
                  const zIndex = window.getComputedStyle(el).zIndex;
                  if (zIndex && parseInt(zIndex) > 1000) {
                    const rect = el.getBoundingClientRect();
                    // If it covers most of the screen, it's likely an ad overlay
                    if (rect.width > window.innerWidth * 0.5 && rect.height > window.innerHeight * 0.5) {
                      el.remove();
                      console.log('🗑️ Removed high z-index overlay:', zIndex);
                    }
                  }
                });
                
                // 4. Block new window.open calls inside iframe
                if (iframe.contentWindow.open) {
                  iframe.contentWindow.open = function() {
                    console.log('🚫 Blocked iframe popup');
                    return null;
                  };
                }
              }
            } catch (corsError) {
              // CORS prevents access - this is expected for cross-origin iframes
              // We can't access the iframe content, but we've blocked popups at the window level
            }
          }
        } catch (e) {
          // Silently handle errors
        }
      }
    }, 500); // Check every 500ms for faster ad removal

    return () => {
      clearInterval(checkIframeRedirects);
      console.log('🎯 Iframe monitor stopped');
    };
  }, [currentUrl]);

  // If no sources available at all
  if (!wootlyUrl && !doodUrl && !vidsrcUrl) {
    return (
      <div className="fixed inset-0 bg-gradient-to-br from-black via-gray-900 to-black z-50 flex items-center justify-center p-4 backdrop-blur-sm">
        <div className="bg-gradient-to-br from-dark-light to-dark rounded-2xl p-8 max-w-md w-full text-center shadow-2xl border border-gray-800">
          <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-red-500/10 flex items-center justify-center">
            <FiX className="text-primary" size={40} />
          </div>
          <h3 className="text-3xl font-bold text-white mb-3">No Stream Available</h3>
          <p className="text-gray-400 mb-8 leading-relaxed">
            Sorry, this content is not available for streaming at the moment.
          </p>
          <button
            onClick={onClose}
            className="bg-gradient-to-r from-primary to-red-600 hover:from-red-600 hover:to-primary text-white px-8 py-3 rounded-xl font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg"
          >
            Close
          </button>
        </div>
      </div>
    );
  }

  // Get server display name
  const getServerName = (source) => {
    switch (source) {
      case 'vidsrc': return 'VidSrc TO';
      case 'vidsrc2': return 'VidSrc XYZ';
      case 'vidsrc3': return 'VidSrc ME';
      case 'vidsrc4': return 'VidSrc NET';
      case 'vidsrc5': return 'VidSrc CC';
      case 'wootly': return 'Wootly';
      case 'dood': return 'Dood';
      default: return 'Unknown';
    }
  };

  // Available servers
  const availableServers = [
    vidsrcUrl && { id: 'vidsrc', name: 'VidSrc TO', badge: 'Primary' },
    vidsrcUrls.vidsrc2 && { id: 'vidsrc2', name: 'VidSrc XYZ', badge: 'Alt 1' },
    vidsrcUrls.vidsrc3 && { id: 'vidsrc3', name: 'VidSrc ME', badge: 'Alt 2' },
    vidsrcUrls.vidsrc4 && { id: 'vidsrc4', name: 'VidSrc NET', badge: 'Alt 3' },
    vidsrcUrls.vidsrc5 && { id: 'vidsrc5', name: 'VidSrc CC', badge: 'Alt 4' },
    wootlyUrl && { id: 'wootly', name: 'Wootly', badge: 'HD' },
    doodUrl && { id: 'dood', name: 'Dood', badge: 'Fast' },
  ].filter(Boolean);

  return (
    <div className="fixed inset-0 bg-black z-50 flex flex-col">
      {/* Minimalist Header */}
      <div className="absolute top-0 left-0 right-0 z-10 bg-gradient-to-b from-black/80 via-black/40 to-transparent p-6">
        <div className="flex items-center justify-between">
          {/* Title */}
          <div className="flex-1 pr-4">
            <h2 className="text-2xl font-bold text-white drop-shadow-lg line-clamp-1">
              {title}
            </h2>
            <p className="text-sm text-gray-300 mt-1">
              Playing on <span className="text-primary font-semibold">{getServerName(selectedSource)}</span>
            </p>
          </div>

          {/* Close Button */}
          <button
            onClick={onClose}
            className="player-close-btn w-12 h-12 rounded-full bg-white/10 hover:bg-white/20 backdrop-blur-md text-white transition-all duration-300 flex items-center justify-center group border border-white/20"
            aria-label="Close player"
          >
            <FiX size={24} className="group-hover:rotate-90 transition-transform duration-300" />
          </button>
        </div>
      </div>

      {/* Video Player */}
      <div className="flex-1 flex items-center justify-center bg-black relative">
        {currentUrl ? (
          <iframe
            ref={iframeRef}
            src={currentUrl}
            className="w-full h-full"
            frameBorder="0"
            allowFullScreen
            sandbox="allow-same-origin allow-scripts allow-forms allow-popups-to-escape-sandbox"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"
            title={title}
            referrerPolicy="no-referrer"
          />
        ) : (
          <div className="text-center">
            <div className="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-primary mx-auto mb-4"></div>
            <p className="text-gray-400 text-lg">Loading player...</p>
          </div>
        )}
      </div>

      {/* Floating Server Menu */}
      {availableServers.length > 1 && (
        <div className="absolute bottom-8 right-8 z-20">
          {/* Server Menu Dropdown */}
          {showServerMenu && (
            <div className="mb-3 bg-dark-light/95 backdrop-blur-xl rounded-2xl shadow-2xl border border-gray-700 overflow-hidden animate-slideUp">
              <div className="p-3">
                <p className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-2 px-2">
                  Select Server
                </p>
                <div className="space-y-1">
                  {availableServers.map((server) => (
                    <button
                      key={server.id}
                      onClick={() => {
                        setSelectedSource(server.id);
                        setShowServerMenu(false);
                      }}
                      className={`w-full flex items-center justify-between px-4 py-3 rounded-xl transition-all duration-200 ${
                        selectedSource === server.id
                          ? 'bg-gradient-to-r from-primary to-red-600 text-white shadow-lg'
                          : 'bg-dark hover:bg-dark-lighter text-gray-300 hover:text-white'
                      }`}
                    >
                      <div className="flex items-center space-x-3">
                        <FiServer size={18} />
                        <span className="font-semibold">{server.name}</span>
                      </div>
                      {server.badge && (
                        <span className={`text-xs px-2 py-1 rounded-full ${
                          selectedSource === server.id
                            ? 'bg-white/20'
                            : 'bg-primary/20 text-primary'
                        }`}>
                          {server.badge}
                        </span>
                      )}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Floating Button */}
          <button
            onClick={() => setShowServerMenu(!showServerMenu)}
            className="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-red-600 hover:from-red-600 hover:to-primary text-white shadow-2xl transition-all duration-300 transform hover:scale-110 flex items-center justify-center group border-2 border-white/20"
            aria-label="Change server"
          >
            <FiServer 
              size={24} 
              className={`transition-transform duration-300 ${showServerMenu ? 'rotate-180' : ''}`}
            />
          </button>
        </div>
      )}

      {/* Click outside to close menu */}
      {showServerMenu && (
        <div
          className="fixed inset-0 z-10"
          onClick={() => setShowServerMenu(false)}
        />
      )}

      {/* Custom CSS for animations and ad blocking */}
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-slideUp {
          animation: slideUp 0.2s ease-out;
        }
        
        /* Enhanced Ad Blocking CSS */
        iframe {
          pointer-events: auto !important;
        }
        
        /* Hide common ad elements */
        [class*="ad-container"],
        [id*="ad-container"],
        [class*="advertisement"],
        [id*="advertisement"],
        [class*="ad-banner"],
        [id*="ad-banner"],
        [class*="popup-ad"],
        [id*="popup-ad"],
        [class*="overlay-ad"],
        [id*="overlay-ad"],
        .ad-overlay,
        .popup-overlay,
        .video-overlay-ad,
        div[style*="position: absolute"][style*="z-index: 999"],
        div[style*="position: fixed"][style*="z-index: 999"],
        div[style*="position: absolute"][style*="z-index: 9999"],
        div[style*="position: fixed"][style*="z-index: 9999"] {
          display: none !important;
          visibility: hidden !important;
          opacity: 0 !important;
          pointer-events: none !important;
          width: 0 !important;
          height: 0 !important;
        }
        
        /* Block ad iframes */
        iframe[src*="doubleclick"],
        iframe[src*="googlesyndication"],
        iframe[src*="googleadservices"],
        iframe[src*="/ads/"],
        iframe[src*="ad."],
        iframe[src*="ads."],
        iframe[src*="adservice"],
        iframe[src*="advertising"] {
          display: none !important;
          visibility: hidden !important;
          width: 0 !important;
          height: 0 !important;
        }
      `}} />
    </div>
  );
};

export default VideoPlayer;