webpackJsonp(["pages.projects.jobs.show"], {
    "../../../node_modules/visibilityjs/index.js": function(t, e, i) {
        t.exports = i("../../../node_modules/visibilityjs/lib/visibility.timers.js")
    },
    "../../../node_modules/visibilityjs/lib/visibility.core.js": function(t, e) { !
        function(e) {
            "use strict";
            var i = -1,
            s = {
                onVisible: function(t) {
                    var e = s.isSupported();
                    if (!e || !s.hidden()) return t(),
                    e;
                    var i = s.change(function(e, n) {
                        s.hidden() || (s.unbind(i), t())
                    });
                    return i
                },
                change: function(t) {
                    if (!s.isSupported()) return ! 1;
                    i += 1;
                    var e = i;
                    return s._callbacks[e] = t,
                    s._listen(),
                    e
                },
                unbind: function(t) {
                    delete s._callbacks[t]
                },
                afterPrerendering: function(t) {
                    var e = s.isSupported();
                    if (!e || "prerender" != s.state()) return t(),
                    e;
                    var i = s.change(function(e, n) {
                        "prerender" != n && (s.unbind(i), t())
                    });
                    return i
                },
                hidden: function() {
                    return ! (!s._doc.hidden && !s._doc.webkitHidden)
                },
                state: function() {
                    return s._doc.visibilityState || s._doc.webkitVisibilityState || "visible"
                },
                isSupported: function() {
                    return ! (!s._doc.visibilityState && !s._doc.webkitVisibilityState)
                },
                _doc: document || {},
                _callbacks: {},
                _change: function(t) {
                    var e = s.state();
                    for (var i in s._callbacks) s._callbacks[i].call(s._doc, t, e)
                },
                _listen: function() {
                    if (!s._init) {
                        var t = "visibilitychange";
                        s._doc.webkitVisibilityState && (t = "webkit" + t);
                        var e = function() {
                            s._change.apply(s, arguments)
                        };
                        s._doc.addEventListener ? s._doc.addEventListener(t, e) : s._doc.attachEvent(t, e),
                        s._init = !0
                    }
                }
            };
            void 0 !== t && t.exports ? t.exports = s: e.Visibility = s
        } (this)
    },
    "../../../node_modules/visibilityjs/lib/visibility.timers.js": function(t, e, i) { !
        function(e) {
            "use strict";
            var s = -1,
            n = function(t) {
                return t.every = function(e, i, n) {
                    t._time(),
                    n || (n = i, i = null),
                    s += 1;
                    var o = s;
                    return t._timers[o] = {
                        visible: e,
                        hidden: i,
                        callback: n
                    },
                    t._run(o, !1),
                    t.isSupported() && t._listen(),
                    o
                },
                t.stop = function(e) {
                    return !! t._timers[e] && (t._stop(e), delete t._timers[e], !0)
                },
                t._timers = {},
                t._time = function() {
                    t._timed || (t._timed = !0, t._wasHidden = t.hidden(), t.change(function() {
                        t._stopRun(),
                        t._wasHidden = t.hidden()
                    }))
                },
                t._run = function(i, s) {
                    var n, o = t._timers[i];
                    if (t.hidden()) {
                        if (null === o.hidden) return;
                        n = o.hidden
                    } else n = o.visible;
                    var a = function() {
                        o.last = new Date,
                        o.callback.call(e)
                    };
                    if (s) {
                        var r = new Date,
                        l = r - o.last;
                        n > l ? o.delay = setTimeout(function() {
                            o.id = setInterval(a, n),
                            a()
                        },
                        n - l) : (o.id = setInterval(a, n), a())
                    } else o.id = setInterval(a, n)
                },
                t._stop = function(e) {
                    var i = t._timers[e];
                    clearInterval(i.id),
                    clearTimeout(i.delay),
                    delete i.id,
                    delete i.delay
                },
                t._stopRun = function(e) {
                    var i = t.hidden(),
                    s = t._wasHidden;
                    if (i && !s || !i && s) for (var n in t._timers) t._stop(n),
                    t._run(n, !i)
                },
                t
            };
            void 0 !== t && t.exports ? t.exports = n(i("../../../node_modules/visibilityjs/lib/visibility.core.js")) : n(e.Visibility)
        } (window)
    },
    "../images/no_avatar.png": function(t, e) {
        t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAABLCAAAAAAdJSU2AAACNElEQVR4AdXYBa7jMBCA4b3/JZahzIkjp2qt+BWUWnG5ln2XxaJJb2b5F2ukL4wvzK/rP7bUcbf92u6oftLSe1ldk8efsfaVeEjusZZeC6e1RllaCk/yG6ag1lZ4WwPX69uyD6tAe/g2ipAlNMRS37awDLaFrpcMWxXQOi0jnWCWjFkSZomYJWDWKmatYNZyEWkJsvQimoZYah5NgdaLxagCtF6GRy0DshZPkeYwS/KIJWGWYjwYUzDLxCwDtJ54OKglimBLqHWahii2g1pmHLLGBmwVoRjcKlmgOdw65H5qKuGWCVi5Qlhs6m1sENZi4q3AWNvca5UYy2RjT/SAsiZey6CsIvc0wVlV5lJ0ibPMyLUGCmlxQq0IM0hLdWyro7CWEc3sXsqaK4O2zLxOsmtpfW5Q1u68ZrVmepaaNXEewawtI9X5Xl3U3n1qND6+rfPzvqoIWz/fklNCSLY153YV53J/XUxGCJnKZ1lajsn3/Ffegf6Y5pV2LUsSNL2UHzxUfh3TlYpZqqTpXZm0KZk9zJcqaEmaWPHDw0pxe05K7bWOLHFLWXVetqpYmrjle4+1y0aBaF4UOQ1NU+lYezJClkjLUnSEjqhH6zjAW4OjtY39Ibq+sawUb6W2RQfoqG0VeKuwrRJvlba17faRdbe2pTtYq6Nty/S7yAbGsQjWIq41wVoT1+IdZNy1djUcVdu5lklQWC0xHkt1X31qNEE1Pr3qKv/9XiSNj6Aaifj3/69+AYujsR/MvkpZAAAAAElFTkSuQmCC"
    },
    "./build_variables.js": function(t, e, i) {
        "use strict"; (function(t) {
            function i() {
                t(".js-reveal-variables").off("click").on("click",
                function() {
                    t(".js-build-variables").toggle(),
                    t(this).hide()
                })
            }
            e.a = i
        }).call(e, i("../../../node_modules/jquery/dist/jquery.js"))
    },
    "./job.js": function(t, e, i) {
        "use strict"; (function(t) {
            function s(t, e) {
                if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
            }
            var n = i("../../../node_modules/underscore/underscore.js"),
            o = i.n(n),
            a = i("./lib/utils/axios_utils.js"),
            r = i("./lib/utils/url_utility.js"),
            l = i("./breakpoints.js"),
            u = i("./lib/utils/number_utils.js"),
            c = i("./lib/utils/common_utils.js"),
            d = function() {
                function t(t, e) {
                    for (var i = 0; i < e.length; i++) {
                        var s = e[i];
                        s.enumerable = s.enumerable || !1,
                        s.configurable = !0,
                        "value" in s && (s.writable = !0),
                        Object.defineProperty(t, s.key, s)
                    }
                }
                return function(e, i, s) {
                    return i && t(e.prototype, i),
                    s && t(e, s),
                    e
                }
            } (),
            h = function() {
                function e(i) {
                    var n = this;
                    s(this, e),
                    this.timeout = null,
                    this.state = null,
                    this.fetchingStatusFavicon = !1,
                    this.options = i || t(".js-build-options").data(),
                    this.pagePath = this.options.pagePath,
                    this.buildStatus = this.options.buildStatus,
                    this.state = this.options.logState,
                    this.buildStage = this.options.buildStage,
                    this.$document = t(document),
                    this.$window = t(window),
                    this.logBytes = 0,
                    this.updateDropdown = this.updateDropdown.bind(this),
                    this.$buildTrace = t("#build-trace"),
                    this.$buildRefreshAnimation = t(".js-build-refresh"),
                    this.$truncatedInfo = t(".js-truncated-info"),
                    this.$buildTraceOutput = t(".js-build-output"),
                    this.$topBar = t(".js-top-bar"),
                    this.$scrollTopBtn = t(".js-scroll-up"),
                    this.$scrollBottomBtn = t(".js-scroll-down"),
                    clearTimeout(this.timeout),
                    this.initSidebar(),
                    this.populateJobs(this.buildStage),
                    this.updateStageDropdownText(this.buildStage),
                    this.sidebarOnResize(),
                    this.$document.off("click", ".js-sidebar-build-toggle").on("click", ".js-sidebar-build-toggle", this.sidebarOnClick.bind(this)),
                    this.$document.off("click", ".stage-item").on("click", ".stage-item", this.updateDropdown),
                    this.$scrollTopBtn.off("click").on("click", this.scrollToTop.bind(this)),
                    this.$scrollBottomBtn.off("click").on("click", this.scrollToBottom.bind(this)),
                    this.scrollThrottled = o.a.throttle(this.toggleScroll.bind(this), 100),
                    this.$window.off("scroll").on("scroll",
                    function() {
                        n.isScrolledToBottom() ? n.isScrolledToBottom() && !n.isLogComplete && n.toggleScrollAnimation(!0) : n.toggleScrollAnimation(!1),
                        n.scrollThrottled()
                    }),
                    this.$window.off("resize.build").on("resize.build", o.a.throttle(this.sidebarOnResize.bind(this), 100)),
                    this.initAffixTopArea(),
                    this.getBuildTrace()
                }
                return d(e, [{
                    key: "initAffixTopArea",
                    value: function() {
                        if ("static" === this.$topBar.css("position")) {
                            var t = this.$buildTrace.offset().top;
                            this.$topBar.affix({
                                offset: {
                                    top: t
                                }
                            })
                        }
                    }
                },
                {
                    key: "canScroll",
                    value: function() {
                        return t(document).height() > t(window).height()
                    }
                },
                {
                    key: "toggleScroll",
                    value: function() {
                        var e = t(document),
                        i = e.scrollTop(),
                        s = e.height(),
                        n = t(window).height();
                        this.canScroll() ? i > 0 && s - i !== n ? (this.toggleDisableButton(this.$scrollTopBtn, !1), this.toggleDisableButton(this.$scrollBottomBtn, !1)) : 0 === i ? (this.toggleDisableButton(this.$scrollTopBtn, !0), this.toggleDisableButton(this.$scrollBottomBtn, !1)) : this.isScrolledToBottom() && (this.toggleDisableButton(this.$scrollTopBtn, !1), this.toggleDisableButton(this.$scrollBottomBtn, !0)) : (this.toggleDisableButton(this.$scrollTopBtn, !0), this.toggleDisableButton(this.$scrollBottomBtn, !0))
                    }
                },
                {
                    key: "isScrolledToBottom",
                    value: function() {
                        var e = t(document),
                        i = e.scrollTop();
                        return e.height() - i === t(window).height()
                    }
                },
                {
                    key: "scrollDown",
                    value: function() {
                        var e = t(document);
                        e.scrollTop(e.height())
                    }
                },
                {
                    key: "scrollToBottom",
                    value: function() {
                        this.scrollDown(),
                        this.hasBeenScrolled = !0,
                        this.toggleScroll()
                    }
                },
                {
                    key: "scrollToTop",
                    value: function() {
                        t(document).scrollTop(0),
                        this.hasBeenScrolled = !0,
                        this.toggleScroll()
                    }
                },
                {
                    key: "toggleDisableButton",
                    value: function(t, e) {
                        e && t.prop("disabled") || t.prop("disabled", e)
                    }
                },
                {
                    key: "toggleScrollAnimation",
                    value: function(t) {
                        this.$scrollBottomBtn.toggleClass("animate", t)
                    }
                },
                {
                    key: "initSidebar",
                    value: function() {
                        this.$sidebar = t(".js-build-sidebar")
                    }
                },
                {
                    key: "getBuildTrace",
                    value: function() {
                        var e = this;
                        return a.a.get(this.pagePath + "/trace.json", {
                            params: {
                                state: this.state
                            }
                        }).then(function(i) {
                            var s = i.data;
                            if (e.fetchingStatusFavicon || (e.fetchingStatusFavicon = !0, Object(c.E)(e.pagePath + "/status.json").then(function() {
                                e.fetchingStatusFavicon = !1
                            }).
                            catch(function() {
                                e.fetchingStatusFavicon = !1
                            })), s.state && (e.state = s.state), e.isScrollInBottom = e.isScrolledToBottom(), s.append ? (e.$buildTraceOutput.append(s.html), e.logBytes += s.size) : (e.$buildTraceOutput.html(s.html), e.logBytes = s.size), e.logBytes < s.total) {
                                var n = Object(u.c)(e.logBytes);
                                t(".js-truncated-info-size").html("" + n),
                                e.$truncatedInfo.removeClass("hidden")
                            } else e.$truncatedInfo.addClass("hidden");
                            e.isLogComplete = s.complete,
                            !1 === s.complete ? e.timeout = setTimeout(function() {
                                e.getBuildTrace()
                            },
                            4e3) : (e.$buildRefreshAnimation.remove(), e.toggleScrollAnimation(!1)),
                            s.status !== e.buildStatus && Object(r.g)(e.pagePath)
                        }).
                        catch(function() {
                            e.$buildRefreshAnimation.remove()
                        }).then(function() {
                            e.isScrollInBottom && e.scrollDown()
                        }).then(function() {
                            return e.toggleScroll()
                        })
                    }
                },
                {
                    key: "shouldHideSidebarForViewport",
                    value: function() {
                        var t = l.a.getBreakpointSize();
                        return "xs" === t || "sm" === t
                    }
                },
                {
                    key: "toggleSidebar",
                    value: function(e) {
                        var i = "boolean" == typeof e ? !e: void 0,
                        s = t(".js-sidebar-build-toggle-header");
                        this.$sidebar.toggleClass("right-sidebar-expanded", i).toggleClass("right-sidebar-collapsed", e),
                        this.$topBar.toggleClass("sidebar-expanded", i).toggleClass("sidebar-collapsed", e),
                        this.$sidebar.hasClass("right-sidebar-expanded") ? s.addClass("hidden") : s.removeClass("hidden")
                    }
                },
                {
                    key: "sidebarOnResize",
                    value: function() {
                        this.toggleSidebar(this.shouldHideSidebarForViewport())
                    }
                },
                {
                    key: "sidebarOnClick",
                    value: function() {
                        this.shouldHideSidebarForViewport() && this.toggleSidebar()
                    }
                },
                {
                    key: "populateJobs",
                    value: function(e) {
                        t(".build-job").hide(),
                        t('.build-job[data-stage="' + e + '"]').show()
                    }
                },
                {
                    key: "updateStageDropdownText",
                    value: function(e) {
                        t(".stage-selection").text(e)
                    }
                },
                {
                    key: "updateDropdown",
                    value: function(t) {
                        t.preventDefault();
                        var e = t.currentTarget.text;
                        this.updateStageDropdownText(e),
                        this.populateJobs(e)
                    }
                }]),
                e
            } ();
            e.a = h
        }).call(e, i("../../../node_modules/jquery/dist/jquery.js"))
    },
    "./lib/utils/constants.js": function(t, e, i) {
        "use strict";
        i.d(e, "a",
        function() {
            return s
        }),
        i.d(e, "b",
        function() {
            return n
        });
        var s = 1024,
        n = "hidden"
    },
    "./lib/utils/http_status.js": function(t, e, i) {
        "use strict";
        e.a = {
            ABORTED: 0,
            NO_CONTENT: 204,
            OK: 200,
            MULTIPLE_CHOICES: 300,
            BAD_REQUEST: 400,
            NOT_FOUND: 404
        }
    },
    "./lib/utils/number_utils.js": function(t, e, i) {
        "use strict";
        function s(t) {
            var e = "",
            i = 0,
            s = "";
            if (!isNaN(Number(t))) {
                switch (e = t.toString().split(".")[0], e.length) {
                case 1:
                    i = 3;
                    break;
                case 2:
                    i = 2;
                    break;
                case 3:
                    i = 1;
                    break;
                default:
                    i = 4
                }
                s = Number(t).toFixed(i)
            }
            return s
        }
        function n(t) {
            return t / l.a
        }
        function o(t) {
            return t / (l.a * l.a)
        }
        function a(t) {
            return t / (l.a * l.a * l.a)
        }
        function r(t) {
            return t < l.a ? t + " bytes": t < l.a * l.a ? n(t).toFixed(2) + " KiB": t < l.a * l.a * l.a ? o(t).toFixed(2) + " MiB": a(t).toFixed(2) + " GiB"
        }
        e.b = s,
        e.a = o,
        e.c = r;
        var l = i("./lib/utils/constants.js")
    },
    "./lib/utils/poll.js": function(t, e, i) {
        "use strict";
        function s(t, e) {
            if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
        }
        var n = i("./lib/utils/http_status.js"),
        o = i("./lib/utils/common_utils.js"),
        a = function() {
            function t(t, e) {
                for (var i = 0; i < e.length; i++) {
                    var s = e[i];
                    s.enumerable = s.enumerable || !1,
                    s.configurable = !0,
                    "value" in s && (s.writable = !0),
                    Object.defineProperty(t, s.key, s)
                }
            }
            return function(e, i, s) {
                return i && t(e.prototype, i),
                s && t(e, s),
                e
            }
        } (),
        r = function() {
            function t() {
                var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                s(this, t),
                this.options = e,
                this.options.data = e.data || {},
                this.options.notificationCallback = e.notificationCallback ||
                function() {},
                this.intervalHeader = "POLL-INTERVAL",
                this.timeoutID = null,
                this.canPoll = !0
            }
            return a(t, [{
                key: "checkConditions",
                value: function(t) {
                    var e = this,
                    i = Object(o.x)(t.headers),
                    s = parseInt(i[this.intervalHeader], 10);
                    s > 0 && t.status === n.a.OK && this.canPoll && (this.timeoutID = setTimeout(function() {
                        e.makeRequest()
                    },
                    s)),
                    this.options.successCallback(t)
                }
            },
            {
                key: "makeRequest",
                value: function() {
                    var t = this,
                    e = this.options,
                    i = e.resource,
                    s = e.method,
                    o = e.data,
                    a = e.errorCallback,
                    r = e.notificationCallback;
                    return r(!0),
                    i[s](o).then(function(e) {
                        t.checkConditions(e),
                        r(!1)
                    }).
                    catch(function(t) {
                        r(!1),
                        t.status !== n.a.ABORTED && a(t)
                    })
                }
            },
            {
                key: "stop",
                value: function() {
                    this.canPoll = !1,
                    clearTimeout(this.timeoutID)
                }
            },
            {
                key: "restart",
                value: function(t) {
                    t && t.data && (this.options.data = t.data),
                    this.canPoll = !0,
                    this.makeRequest()
                }
            }]),
            t
        } ();
        e.a = r
    },
    "./pages/projects/jobs/show/index.js": function(t, e, i) {
        "use strict";
        function s(t, e) {
            if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
        }
        function n(t, e) {
            if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
        }
        function o(t, e) {
            if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
        }
        Object.defineProperty(e, "__esModule", {
            value: !0
        });
        var a = i("../../../node_modules/vue/dist/vue.esm.js"),
        r = i("../../../node_modules/visibilityjs/index.js"),
        l = i.n(r),
        u = i("./flash.js"),
        c = i("./lib/utils/poll.js"),
        d = function() {
            function t(t, e) {
                for (var i = 0; i < e.length; i++) {
                    var s = e[i];
                    s.enumerable = s.enumerable || !1,
                    s.configurable = !0,
                    "value" in s && (s.writable = !0),
                    Object.defineProperty(t, s.key, s)
                }
            }
            return function(e, i, s) {
                return i && t(e.prototype, i),
                s && t(e, s),
                e
            }
        } (),
        h = function() {
            function t() {
                s(this, t),
                this.state = {
                    job: {}
                }
            }
            return d(t, [{
                key: "storeJob",
                value: function() {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    this.state.job = t
                }
            }]),
            t
        } (),
        b = h,
        p = i("./lib/utils/axios_utils.js"),
        f = function() {
            function t(t, e) {
                for (var i = 0; i < e.length; i++) {
                    var s = e[i];
                    s.enumerable = s.enumerable || !1,
                    s.configurable = !0,
                    "value" in s && (s.writable = !0),
                    Object.defineProperty(t, s.key, s)
                }
            }
            return function(e, i, s) {
                return i && t(e.prototype, i),
                s && t(e, s),
                e
            }
        } (),
        m = function() {
            function t(e) {
                n(this, t),
                this.job = e
            }
            return f(t, [{
                key: "getJob",
                value: function() {
                    return p.a.get(this.job)
                }
            }]),
            t
        } (),
        v = m,
        g = i("./job.js"),
        _ = i("./build_variables.js"),
        j = function() {
            function t(t, e) {
                for (var i = 0; i < e.length; i++) {
                    var s = e[i];
                    s.enumerable = s.enumerable || !1,
                    s.configurable = !0,
                    "value" in s && (s.writable = !0),
                    Object.defineProperty(t, s.key, s)
                }
            }
            return function(e, i, s) {
                return i && t(e.prototype, i),
                s && t(e, s),
                e
            }
        } (),
        y = function() {
            function t() {
                var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                o(this, t),
                this.options = e,
                this.store = new b,
                this.service = new v(e.endpoint),
                this.state = {
                    isLoading: !1
                }
            }
            return j(t, [{
                key: "initBuildClass",
                value: function() {
                    this.build = new g.a,
                    Object(_.a)()
                }
            },
            {
                key: "fetchJob",
                value: function() {
                    var t = this;
                    this.poll = new c.a({
                        resource: this.service,
                        method: "getJob",
                        successCallback: function(e) {
                            return t.successCallback(e)
                        },
                        errorCallback: function() {
                            return t.errorCallback()
                        }
                    }),
                    l.a.hidden() ? this.getJob() : (this.state.isLoading = !0, this.poll.makeRequest()),
                    l.a.change(function() {
                        l.a.hidden() ? t.poll.stop() : t.poll.restart()
                    })
                }
            },
            {
                key: "getJob",
                value: function() {
                    var t = this;
                    return this.service.getJob().then(function(e) {
                        return t.successCallback(e)
                    }).
                    catch(function() {
                        return t.errorCallback()
                    })
                }
            },
            {
                key: "successCallback",
                value: function(t) {
                    return this.state.isLoading = !1,
                    this.store.storeJob(t.data)
                }
            },
            {
                key: "errorCallback",
                value: function() {
                    return this.state.isLoading = !1,
                    new u.a("An error occurred while fetching the job.")
                }
            }]),
            t
        } (),
        k = y,
        w = i("./vue_shared/components/header_ci_component.vue"),
        C = i("./vue_shared/components/loading_icon.vue"),
        S = {
            name: "JobHeaderSection",
            components: {
                ciHeader: w.a,
                loadingIcon: C.a
            },
            props: {
                job: {
                    type: Object,
                    required: !0
                },
                isLoading: {
                    type: Boolean,
                    required: !0
                }
            },
            data: function() {
                return {
                    actions: this.getActions()
                }
            },
            computed: {
                status: function() {
                    return this.job && this.job.status
                },
                shouldRenderContent: function() {
                    return ! this.isLoading && Object.keys(this.job).length
                },
                jobStarted: function() {
                    return ! 1 == !this.job.started
                }
            },
            watch: {
                job: function() {
                    this.actions = this.getActions()
                }
            },
            methods: {
                getActions: function() {
                    var t = [];
                    return this.job.new_issue_path && t.push({
                        label: "New issue",
                        path: this.job.new_issue_path,
                        cssClass: "js-new-issue btn btn-new btn-inverted visible-md-block visible-lg-block",
                        type: "link"
                    }),
                    t
                }
            }
        },
        B = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("div", {
                staticClass: "js-build-header build-header top-area"
            },
            [t.shouldRenderContent ? i("ci-header", {
                attrs: {
                    status: t.status,
                    "item-name": "Job",
                    "item-id": t.job.id,
                    time: t.job.created_at,
                    user: t.job.user,
                    actions: t.actions,
                    "has-sidebar-button": !0,
                    "should-render-triggered-label": t.jobStarted
                }
            }) : t._e(), t._v(" "), t.isLoading ? i("loading-icon", {
                staticClass: "prepend-top-default append-bottom-default",
                attrs: {
                    size: "2"
                }
            }) : t._e()], 1)
        },
        T = [],
        q = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        x = Object(q.a)(S, B, T, !1, null, null, null),
        A = x.exports,
        O = {
            name: "SidebarDetailRow",
            props: {
                title: {
                    type: String,
                    required: !1,
                default:
                    ""
                },
                value: {
                    type: String,
                    required: !0
                }
            },
            computed: {
                hasTitle: function() {
                    return this.title.length > 0
                }
            }
        },
        z = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("p", {
                staticClass: "build-detail-row"
            },
            [t.hasTitle ? i("span", {
                staticClass: "build-light-text"
            },
            [t._v("\n    " + t._s(t.title) + ":\n  ")]) : t._e(), t._v("\n  " + t._s(t.value) + "\n")])
        },
        L = [],
        $ = Object(q.a)(O, z, L, !1, null, null, null),
        E = $.exports,
        N = i("./vue_shared/mixins/timeago.js"),
        D = i("./lib/utils/datetime_utility.js"),
        R = {
            name: "SidebarDetailsBlock",
            components: {
                detailRow: E,
                loadingIcon: C.a
            },
            mixins: [N.a],
            props: {
                job: {
                    type: Object,
                    required: !0
                },
                isLoading: {
                    type: Boolean,
                    required: !0
                }
            },
            computed: {
                shouldRenderContent: function() {
                    return ! this.isLoading && Object.keys(this.job).length > 0
                },
                coverage: function() {
                    return this.job.coverage + "%"
                },
                duration: function() {
                    return Object(D.k)(this.job.duration)
                },
                queued: function() {
                    return Object(D.k)(this.job.queued)
                },
                runnerId: function() {
                    return "#" + this.job.runner.id
                },
                renderBlock: function() {
                    return this.job.merge_request || this.job.duration || this.job.finished_data || this.job.erased_at || this.job.queued || this.job.runner || this.job.coverage || this.job.tags.length || this.job.cancel_path
                }
            }
        },
        I = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("div", [t.shouldRenderContent ? [t.job.retry_path || t.job.new_issue_path ? i("div", {
                staticClass: "block retry-link"
            },
            [t.job.new_issue_path ? i("a", {
                staticClass: "js-new-issue btn btn-new btn-inverted",
                attrs: {
                    href: t.job.new_issue_path
                }
            },
            [t._v("\n        New issue\n      ")]) : t._e(), t._v(" "), t.job.retry_path ? i("a", {
                staticClass: "js-retry-job btn btn-inverted-secondary",
                attrs: {
                    href: t.job.retry_path,
                    "data-method": "post",
                    rel: "nofollow"
                }
            },
            [t._v("\n        Retry\n      ")]) : t._e()]) : t._e(), t._v(" "), i("div", {
                class: {
                    block: t.renderBlock
                }
            },
            [t.job.merge_request ? i("p", {
                staticClass: "build-detail-row js-job-mr"
            },
            [i("span", {
                staticClass: "build-light-text"
            },
            [t._v("\n          Merge Request:\n        ")]), t._v(" "), i("a", {
                attrs: {
                    href: t.job.merge_request.path
                }
            },
            [t._v("\n          !" + t._s(t.job.merge_request.iid) + "\n        ")])]) : t._e(), t._v(" "), t.job.duration ? i("detail-row", {
                staticClass: "js-job-duration",
                attrs: {
                    title: "Duration",
                    value: t.duration
                }
            }) : t._e(), t._v(" "), t.job.finished_at ? i("detail-row", {
                staticClass: "js-job-finished",
                attrs: {
                    title: "Finished",
                    value: t.timeFormated(t.job.finished_at)
                }
            }) : t._e(), t._v(" "), t.job.erased_at ? i("detail-row", {
                staticClass: "js-job-erased",
                attrs: {
                    title: "Erased",
                    value: t.timeFormated(t.job.erased_at)
                }
            }) : t._e(), t._v(" "), t.job.queued ? i("detail-row", {
                staticClass: "js-job-queued",
                attrs: {
                    title: "Queued",
                    value: t.queued
                }
            }) : t._e(), t._v(" "), t.job.runner ? i("detail-row", {
                staticClass: "js-job-runner",
                attrs: {
                    title: "Runner",
                    value: t.runnerId
                }
            }) : t._e(), t._v(" "), t.job.coverage ? i("detail-row", {
                staticClass: "js-job-coverage",
                attrs: {
                    title: "Coverage",
                    value: t.coverage
                }
            }) : t._e(), t._v(" "), t.job.tags.length ? i("p", {
                staticClass: "build-detail-row js-job-tags"
            },
            [i("span", {
                staticClass: "build-light-text"
            },
            [t._v("\n          Tags:\n        ")]), t._v(" "), t._l(t.job.tags,
            function(e, s) {
                return i("span", {
                    key: s,
                    staticClass: "label label-primary"
                },
                [t._v("\n          " + t._s(e) + "\n        ")])
            })], 2) : t._e(), t._v(" "), t.job.cancel_path ? i("div", {
                staticClass: "btn-group prepend-top-5",
                attrs: {
                    role: "group"
                }
            },
            [i("a", {
                staticClass: "js-cancel-job btn btn-sm btn-default",
                attrs: {
                    href: t.job.cancel_path,
                    "data-method": "post",
                    rel: "nofollow"
                }
            },
            [t._v("\n          Cancel\n        ")])]) : t._e()], 1)] : t._e(), t._v(" "), t.isLoading ? i("loading-icon", {
                staticClass: "prepend-top-10",
                attrs: {
                    size: "2"
                }
            }) : t._e()], 2)
        },
        J = [],
        P = Object(q.a)(R, I, J, !1, null, null, null),
        F = P.exports,
        W = function() {
            var t = document.getElementById("js-job-details-vue").dataset,
            e = new k({
                endpoint: t.endpoint
            });
            e.fetchJob(),
            new a.a({
                el: "#js-build-header-vue",
                components: {
                    jobHeader: A
                },
                data: function() {
                    return {
                        mediator: e
                    }
                },
                mounted: function() {
                    this.mediator.initBuildClass()
                },
                render: function(t) {
                    return t("job-header", {
                        props: {
                            isLoading: this.mediator.state.isLoading,
                            job: this.mediator.store.state.job
                        }
                    })
                }
            }),
            new a.a({
                el: "#js-details-block-vue",
                components: {
                    detailsBlock: F
                },
                data: function() {
                    return {
                        mediator: e
                    }
                },
                render: function(t) {
                    return t("details-block", {
                        props: {
                            isLoading: this.mediator.state.isLoading,
                            job: this.mediator.store.state.job
                        }
                    })
                }
            })
        };
        document.addEventListener("DOMContentLoaded", W)
    },
    "./vue_shared/components/ci_badge_link.vue": function(t, e, i) {
        "use strict";
        var s = i("./vue_shared/components/ci_icon.vue"),
        n = i("./vue_shared/directives/tooltip.js"),
        o = {
            components: {
                ciIcon: s.a
            },
            directives: {
                tooltip: n.a
            },
            props: {
                status: {
                    type: Object,
                    required: !0
                },
                showText: {
                    type: Boolean,
                    required: !1,
                default:
                    !0
                }
            },
            computed: {
                cssClass: function() {
                    var t = this.status.group;
                    return t ? "ci-status ci-" + t: "ci-status"
                }
            }
        },
        a = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("a", {
                directives: [{
                    name: "tooltip",
                    rawName: "v-tooltip"
                }],
                class: t.cssClass,
                attrs: {
                    href: t.status.details_path,
                    title: t.showText ? "": t.status.text
                }
            },
            [i("ci-icon", {
                attrs: {
                    status: t.status
                }
            }), t._v(" "), t.showText ? [t._v("\n    " + t._s(t.status.text) + "\n  ")] : t._e()], 2)
        },
        r = [],
        l = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        u = Object(l.a)(o, a, r, !1, null, null, null);
        e.a = u.exports
    },
    "./vue_shared/components/ci_icon.vue": function(t, e, i) {
        "use strict";
        var s = i("./vue_shared/components/icon.vue"),
        n = {
            components: {
                icon: s.a
            },
            props: {
                status: {
                    type: Object,
                    required: !0
                }
            },
            computed: {
                cssClass: function() {
                    var t = this.status.group;
                    return "ci-status-icon ci-status-icon-" + t + " js-ci-status-icon-" + t
                }
            }
        },
        o = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("span", {
                class: t.cssClass
            },
            [i("icon", {
                attrs: {
                    name: t.status.icon
                }
            })], 1)
        },
        a = [],
        r = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        l = Object(r.a)(n, o, a, !1, null, null, null);
        e.a = l.exports
    },
    "./vue_shared/components/header_ci_component.vue": function(t, e, i) {
        "use strict";
        var s = i("./vue_shared/components/ci_badge_link.vue"),
        n = i("./vue_shared/components/loading_icon.vue"),
        o = i("./vue_shared/components/time_ago_tooltip.vue"),
        a = i("./vue_shared/directives/tooltip.js"),
        r = i("./vue_shared/components/user_avatar/user_avatar_image.vue"),
        l = {
            components: {
                ciIconBadge: s.a,
                loadingIcon: n.a,
                timeagoTooltip: o.a,
                userAvatarImage: r.a
            },
            directives: {
                tooltip: a.a
            },
            props: {
                status: {
                    type: Object,
                    required: !0
                },
                itemName: {
                    type: String,
                    required: !0
                },
                itemId: {
                    type: Number,
                    required: !0
                },
                time: {
                    type: String,
                    required: !0
                },
                user: {
                    type: Object,
                    required: !1,
                default:
                    function() {
                        return {}
                    }
                },
                actions: {
                    type: Array,
                    required: !1,
                default:
                    function() {
                        return []
                    }
                },
                hasSidebarButton: {
                    type: Boolean,
                    required: !1,
                default:
                    !1
                },
                shouldRenderTriggeredLabel: {
                    type: Boolean,
                    required: !1,
                default:
                    !0
                }
            },
            computed: {
                userAvatarAltText: function() {
                    return this.user.name + "'s avatar"
                }
            },
            methods: {
                onClickAction: function(t) {
                    this.$emit("actionClicked", t)
                }
            }
        },
        u = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("header", {
                staticClass: "page-content-header ci-header-container"
            },
            [i("section", {
                staticClass: "header-main-content"
            },
            [i("ci-icon-badge", {
                attrs: {
                    status: t.status
                }
            }), t._v(" "), i("strong", [t._v("\n        " + t._s(t.itemName) + " #" + t._s(t.itemId) + "\n      ")]), t._v(" "), t.shouldRenderTriggeredLabel ? [t._v("\n        triggered\n      ")] : [t._v("\n        created\n      ")], t._v(" "), i("timeago-tooltip", {
                attrs: {
                    time: t.time
                }
            }), t._v("\n\n      by\n\n      "), t.user ? [i("a", {
                directives: [{
                    name: "tooltip",
                    rawName: "v-tooltip"
                }],
                staticClass: "js-user-link commit-committer-link",
                attrs: {
                    href: t.user.path,
                    title: t.user.email
                }
            },
            [i("user-avatar-image", {
                attrs: {
                    "img-src": t.user.avatar_url,
                    "img-alt": t.userAvatarAltText,
                    "tooltip-text": t.user.name,
                    "img-size": 24
                }
            }), t._v("\n\n          " + t._s(t.user.name) + "\n        ")], 1)] : t._e()], 2), t._v(" "), t.actions.length ? i("section", {
                staticClass: "header-action-buttons"
            },
            [t._l(t.actions,
            function(e, s) {
                return ["link" === e.type ? i("a", {
                    key: s,
                    class: e.cssClass,
                    attrs: {
                        href: e.path
                    }
                },
                [t._v("\n          " + t._s(e.label) + "\n        ")]) : "ujs-link" === e.type ? i("a", {
                    key: s,
                    class: e.cssClass,
                    attrs: {
                        href: e.path,
                        "data-method": "post",
                        rel: "nofollow"
                    }
                },
                [t._v("\n          " + t._s(e.label) + "\n        ")]) : "button" === e.type ? i("button", {
                    key: s,
                    class: e.cssClass,
                    attrs: {
                        disabled: e.isLoading,
                        type: "button"
                    },
                    on: {
                        click: function(i) {
                            t.onClickAction(e)
                        }
                    }
                },
                [t._v("\n          " + t._s(e.label) + "\n          "), i("i", {
                    directives: [{
                        name: "show",
                        rawName: "v-show",
                        value: e.isLoading,
                        expression: "action.isLoading"
                    }],
                    staticClass: "fa fa-spin fa-spinner",
                    attrs: {
                        "aria-hidden": "true"
                    }
                })]) : t._e()]
            }), t._v(" "), t.hasSidebarButton ? i("button", {
                staticClass: "btn btn-default visible-xs-block\nvisible-sm-block sidebar-toggle-btn js-sidebar-build-toggle js-sidebar-build-toggle-header",
                attrs: {
                    type: "button",
                    "aria-label": "Toggle Sidebar",
                    id: "toggleSidebar"
                }
            },
            [i("i", {
                staticClass: "fa fa-angle-double-left",
                attrs: {
                    "aria-hidden": "true",
                    "aria-labelledby": "toggleSidebar"
                }
            })]) : t._e()], 2) : t._e()])
        },
        c = [],
        d = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        h = Object(d.a)(l, u, c, !1, null, null, null);
        e.a = h.exports
    },
    "./vue_shared/components/icon.vue": function(t, e, i) {
        "use strict";
        var s = [8, 12, 16, 18, 24, 32, 48, 72],
        n = {
            props: {
                name: {
                    type: String,
                    required: !0
                },
                size: {
                    type: Number,
                    required: !1,
                default:
                    16,
                    validator: function(t) {
                        return s.includes(t)
                    }
                },
                cssClasses: {
                    type: String,
                    required: !1,
                default:
                    ""
                },
                width: {
                    type: Number,
                    required: !1,
                default:
                    null
                },
                height: {
                    type: Number,
                    required: !1,
                default:
                    null
                },
                y: {
                    type: Number,
                    required: !1,
                default:
                    null
                },
                x: {
                    type: Number,
                    required: !1,
                default:
                    null
                }
            },
            computed: {
                spriteHref: function() {
                    return gon.sprite_icons + "#" + this.name
                },
                iconSizeClass: function() {
                    return this.size ? "s" + this.size: ""
                }
            }
        },
        o = function() {
            var t = this,
            e = t.$createElement,
            i = t._self._c || e;
            return i("svg", {
                class: [t.iconSizeClass, t.cssClasses],
                attrs: {
                    width: t.width,
                    height: t.height,
                    x: t.x,
                    y: t.y
                }
            },
            [i("use", t._b({},
            "use", {
                "xlink:href": t.spriteHref
            },
            !1))])
        },
        a = [],
        r = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        l = Object(r.a)(n, o, a, !1, null, null, null);
        e.a = l.exports
    },
    "./vue_shared/components/time_ago_tooltip.vue": function(t, e, i) {
        "use strict";
        var s = i("./vue_shared/directives/tooltip.js"),
        n = i("./vue_shared/mixins/timeago.js"),
        o = (i("./lib/utils/datetime_utility.js"), {
            directives: {
                tooltip: s.a
            },
            mixins: [n.a],
            props: {
                time: {
                    type: String,
                    required: !0
                },
                tooltipPlacement: {
                    type: String,
                    required: !1,
                default:
                    "top"
                },
                cssClass: {
                    type: String,
                    required: !1,
                default:
                    ""
                }
            }
        }),
        a = function() {
            var t = this,
            e = t.$createElement;
            return (t._self._c || e)("time", {
                directives: [{
                    name: "tooltip",
                    rawName: "v-tooltip"
                }],
                class: t.cssClass,
                attrs: {
                    title: t.tooltipTitle(t.time),
                    "data-placement": t.tooltipPlacement,
                    "data-container": "body"
                }
            },
            [t._v("\n  " + t._s(t.timeFormated(t.time)) + "\n")])
        },
        r = [],
        l = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        u = Object(l.a)(o, a, r, !1, null, null, null);
        e.a = u.exports
    },
    "./vue_shared/components/user_avatar/user_avatar_image.vue": function(t, e, i) {
        "use strict";
        var s = i("../images/no_avatar.png"),
        n = i.n(s),
        o = i("./lazy_loader.js"),
        a = i("./vue_shared/directives/tooltip.js"),
        r = {
            name: "UserAvatarImage",
            directives: {
                tooltip: a.a
            },
            props: {
                lazy: {
                    type: Boolean,
                    required: !1,
                default:
                    !1
                },
                imgSrc: {
                    type: String,
                    required: !1,
                default:
                    n.a
                },
                cssClasses: {
                    type: String,
                    required: !1,
                default:
                    ""
                },
                imgAlt: {
                    type: String,
                    required: !1,
                default:
                    "user avatar"
                },
                size: {
                    type: Number,
                    required: !1,
                default:
                    20
                },
                tooltipText: {
                    type: String,
                    required: !1,
                default:
                    ""
                },
                tooltipPlacement: {
                    type: String,
                    required: !1,
                default:
                    "top"
                }
            },
            computed: {
                sanitizedSource: function() {
                    return "" === this.imgSrc || null === this.imgSrc ? n.a: this.imgSrc
                },
                resultantSrcAttribute: function() {
                    return this.lazy ? o.b: this.sanitizedSource
                },
                tooltipContainer: function() {
                    return this.tooltipText ? "body": null
                },
                avatarSizeClass: function() {
                    return "s" + this.size
                }
            }
        },
        l = function() {
            var t = this,
            e = t.$createElement;
            return (t._self._c || e)("img", {
                directives: [{
                    name: "tooltip",
                    rawName: "v-tooltip"
                }],
                staticClass: "avatar",
                class: (i = {
                    lazy: t.lazy
                },
                i[t.avatarSizeClass] = !0, i[t.cssClasses] = !0, i),
                attrs: {
                    src: t.resultantSrcAttribute,
                    width: t.size,
                    height: t.size,
                    alt: t.imgAlt,
                    "data-src": t.sanitizedSource,
                    "data-container": t.tooltipContainer,
                    "data-placement": t.tooltipPlacement,
                    title: t.tooltipText
                }
            });
            var i
        }, u = [],
        c = i("../../../node_modules/vue-loader/lib/runtime/component-normalizer.js"),
        d = Object(c.a)(r, l, u, !1, null, null, null);
        e.a = d.exports
    },
    "./vue_shared/directives/tooltip.js": function(t, e, i) {
        "use strict"; (function(t) {
            e.a = {
                bind: function(e) {
                    t(e).tooltip()
                },
                componentUpdated: function(e) {
                    t(e).tooltip("fixTitle")
                },
                unbind: function(e) {
                    t(e).tooltip("destroy")
                }
            }
        }).call(e, i("../../../node_modules/jquery/dist/jquery.js"))
    },
    "./vue_shared/mixins/timeago.js": function(t, e, i) {
        "use strict";
        var s = i("./lib/utils/datetime_utility.js");
        e.a = {
            methods: {
                timeFormated: function(t) {
                    return Object(s.f)().format(t)
                },
                tooltipTitle: function(t) {
                    return Object(s.b)(t)
                }
            }
        }
    }
},
["./pages/projects/jobs/show/index.js"]);
//# sourceMappingURL=pages.projects.jobs.show.7da5131627c0d0d055d3.bundle.js.map
